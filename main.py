# Scientific Python Tools
import numpy as np
import matplotlib.pyplot as plt

# PyTorch
from torch import nn, optim
from torch.utils.data import DataLoader

# For the CLI
import argparse
import config


def train():
    pass


def val():
    pass


def test():
    pass


if __name__ == '__main__':
    # Configure Model
    model = config.model
    if config.load_model_path:
        model.load(config.load_model_path)

    if config.use_gpu:
        model.cuda()

    parser = argparse.ArgumentParser(description=f'CLI for {config.model_name}')
    parser.add_argument('--phase', type=str, default='train')
    args = parser.parse_args()

    if args.phase == 'train':
        train()

    elif args.phase == 'test':
        test()

    elif args.phase == 'validate':
        val()

    else:
        raise ValueError('Choose one of train/validate/test')
