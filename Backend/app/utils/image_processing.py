from torchvision import transforms
from PIL import Image
import base64
import io
import torch

# same normalization used during training
MEAN = [0.485, 0.456, 0.406]
STD  = [0.229, 0.224, 0.225]

_preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(MEAN, STD)
])

# to convert a normalized tensor back to PIL image:
_to_pil = transforms.ToPILImage()

def load_image_to_tensor(file):
    """
    file: a file-like object (UploadFile.file)
    Returns: preprocessed tensor with shape [1, C, H, W]
    """
    image = Image.open(file).convert("RGB")
    tensor = _preprocess(image)
    return tensor.unsqueeze(0)  # add batch dim

def denormalize_tensor(tensor):
    """
    tensor: torch.Tensor with shape [1, C, H, W] or [C, H, W]
    returns: tensor in [0,1] range (unpadded) ready for ToPILImage
    """
    t = tensor.detach().cpu().clone()
    if t.dim() == 4:
        t = t.squeeze(0)
    for c, (m, s) in enumerate(zip(MEAN, STD)):
        t[c] = t[c] * s + m
    t = torch.clamp(t, 0, 1)
    return t

def tensor_to_base64(tensor):
    """
    Input: tensor (normalized) shape [1,C,H,W] or [C,H,W]
    Output: base64 PNG string
    """
    img_tensor = denormalize_tensor(tensor)
    pil = _to_pil(img_tensor)
    buf = io.BytesIO()
    pil.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    return b64