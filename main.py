import torch
import argparse
from config import config as cfg
import logging
import coloredlogs

# Setup colorful logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger)


# noinspection PyShadowingNames
def train(model, optimizer, criterion, resume_from_epoch, max_val_accuracy):
    """
    Train the model
    :param model: Model to be trained
    :param optimizer: Method to compute gradients
    :param criterion: Criterion for computing loss
    :param resume_from_epoch: Resume training from this epoch
    :param max_val_accuracy: Save models with greater accuracy on validation set
    """
    for epoch in range(resume_from_epoch, cfg.n_epochs):
        # training
        if epoch % cfg.val_freq == 0:
            # validation & saving best model
            pass


def val(model):
    """
    Check model accuracy on validation set.
    :param model: Model to be tested
    :return: Validation accuracy
    """
    # validation


def test(model):
    # testing
    pass


if __name__ == '__main__':
    # CLI
    parser = argparse.ArgumentParser(description=f'CLI for {config.model_name}')
    parser.add_argument('--phase', type=str, default='train')
    parser.add_argument('--load', type=bool, default=False)
    args = parser.parse_args()

    model = cfg.model
    optimizer = cfg.optimizer
    criterion = cfg.criterion
    resume_from_epoch = cfg.resume_from_epoch
    max_val_accuracy = cfg.max_val_accuracy

    if args.load:
        # Load from checkpoint
        checkpoint = torch.load(cfg.model_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        resume_from_epoch = checkpoint['epoch']
        max_val_accuracy = checkpoint['val_accuracy']

    if args.phase == 'train':
        train(model, optimizer, criterion, resume_from_epoch, max_val_accuracy)

    elif args.phase == 'test':
        test(model)

    else:
        raise ValueError('Choose one of train/validate/test')
