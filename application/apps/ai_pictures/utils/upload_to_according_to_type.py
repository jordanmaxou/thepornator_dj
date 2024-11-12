from os.path import join


def upload_to_according_to_type(instance, filename):
    base_path = "img/aicontent"
    if instance.type == "video":
        base_path = "video/aicontent"
    return join(base_path, filename)
