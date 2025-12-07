from fastapi import FastAPI, UploadFile, File, Form
import torch
from app.models.model_loader import load_model
from app.attacks.fgsm import FGSMAttack
from app.utils.image_processing import load_image_to_tensor, tensor_to_base64

app = FastAPI()

# Load model + class names
model, CLASS_NAMES = load_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize FGSM attack class
attack = FGSMAttack(model)


@app.post("/attack/")
async def generate_attack(
    file: UploadFile = File(...),
    epsilon: float = Form(0.1)
):
    """
    Perform FGSM adversarial attack on uploaded image.
    """

    # 1. Load & preprocess image → tensor [1,3,224,224]
    img_tensor = load_image_to_tensor(file.file).to(device)

    # 2. Get clean prediction
    output = model(img_tensor)
    clean_idx = torch.argmax(output, dim=1).item()
    clean_pred = CLASS_NAMES[clean_idx]

    # 3. Create label tensor (required for loss gradient)
    label = torch.tensor([clean_idx], dtype=torch.long, device=device)

    # 4. Generate adversarial example
    adv_img = attack.generate(img_tensor, label, epsilon)

    # 5. Predict adversarial result
    adv_output = model(adv_img)
    adv_idx = torch.argmax(adv_output, dim=1).item()
    adv_pred = CLASS_NAMES[adv_idx]

    # 6. Convert adversarial image → base64
    adv_base64 = tensor_to_base64(adv_img)

    # 7. Check if attack succeeded
    attack_success = (clean_idx != adv_idx)

    return {
        "clean_prediction": clean_pred,
        "adversarial_prediction": adv_pred,
        "base64_adv_image": adv_base64,
        "attack_success": attack_success,
        "epsilon": epsilon
    }