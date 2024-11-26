from os.path import join


def upload_to_according_to_fake_of_real(instance, filename):
    return join(
        "img/aiornotai", "real" if instance.is_real is True else "fake", filename
    )
