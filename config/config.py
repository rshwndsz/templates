import os
import torch
import torch.nn.functional as F
import torch.optim as optim

# Torch-specific
use_gpu = torch.cuda.is_available()
device = torch.device('cuda' if use_gpu else 'cpu')
num_workers = 4
print_freq = 20
val_freq = 1
resume_from_epoch = 0
max_val_accuracy = 0

# Hyper-parameters
batch_size = 1
n_epochs = 2
lr = 0.01

# Architecture-specific
from models import SampleNet
model_name = 'SampleNet'
model = SampleNet()
model = model.to(device)
criterion = F.cross_entropy
optimizer = optim.Adam(model.parameters())

# Data-specific
project_root = os.getcwd()
dataset_root = os.path.join(project_root, 'datasets', 'dataset_name')
model_path = os.path.join(project_root, 'checkpoints', 'model_final_name.pth')
results_dir = os.path.join(project_root, 'results')

# Import dataset here
train_loader = kidney.train_loader
val_loader = kidney.val_loader
test_loader = kidney.val_loader

