import os
import json
import torch
from torchvision import models

# Paths (relative to backend/)
MODEL_PATH = os.path.join("saved_models", "model.pth")
CLASSES_PATH = os.path.join("saved_models", "classes.json")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    # load class names
    if not os.path.exists(CLASSES_PATH):
        raise FileNotFoundError(f"classes.json not found at {CLASSES_PATH}. Place it there.")
    with open(CLASSES_PATH, "r") as f:
        class_names = json.load(f)

    num_classes = len(class_names)

    # create model and replace final layer
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    # load weights
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Place your fine-tuned model there.")
    state = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(state)

    model = model.to(device)
    model.eval()

    return model, class_names