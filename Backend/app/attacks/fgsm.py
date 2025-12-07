import torch
import torch.nn as nn

class FGSMAttack:
    def __init__(self, model):
        self.model = model
        self.loss_fn = nn.CrossEntropyLoss()

    def generate(self, image, label, epsilon=0.1):
        """
        image: tensor shape [1,C,H,W] (normalized)
        label: tensor shape [1] long (the target label to compute gradient)
        """
        image = image.clone().detach().to(next(self.model.parameters()).device)
        image.requires_grad = True

        self.model.zero_grad()
        outputs = self.model(image)
        loss = self.loss_fn(outputs, label)
        loss.backward()

        gradient = image.grad.data.sign()
        adv_image = image + epsilon * gradient
        # If input was normalized, we clip in normalized space to avoid large out-of-range values.
        # We clip by denormalizing and clipping 0..1 might be safer for visual output,
        # but model input should remain normalized: so we'll clamp unbounded here and
        # rely on tensor_to_base64 to denormalize and clamp for visualization.
        adv_image = torch.clamp(adv_image, -5.0, 5.0)  # keep within some range

        return adv_image.detach()