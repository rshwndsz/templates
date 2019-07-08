import torch.nn.functional as F
import torch.optim as optim

from models import SampleNet


model_name = 'SampleNet'
model = SampleNet()
model = model.to(device)
criterion = F.cross_entropy
optimizer = optim.Adam(model.parameters())