from PIL import Image


def crop_image(img):
    crop_area1 = (0, (img.height - img.width) // 2, img.width, img.height - (img.height - img.width) // 2)
    crop_area2 = (-(img.height - img.width) // 2, 0, img.width + (img.height - img.width) // 2, img.height)

    if img.height > img.width:
        img = img.crop(crop_area1)
    elif img.height < img.width:
        img = img.crop(crop_area2)
    return img


def concat_imgs(imgs_lst):
    cropped_lst = []
    for img in imgs_lst:
        cropped_lst.append(crop_image(img))
    imgs_lst = cropped_lst
    img_h = imgs_lst[0].height
    img_w = imgs_lst[0].width
    dst = Image.new('RGB', (3 * img_w, 3 * img_h))
    for i in range(3):
        for j in range(3):
            dst.paste(imgs_lst[i * 3 + j].resize((img_w, img_h)), (img_w * j, img_h * i))
    dst = dst.resize((500, 500))
    return dst