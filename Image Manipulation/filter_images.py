import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

images = []

def display(title, image):
    display_image = cv2.imread(image)
    plt.figure(figsize=(12,8))
    if len(display_image.shape) == 2:
        plt.imshow(display_image)
    else:
        plt.imshow(cv2.cvtColor(display_image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis("off")
        plt.show()



def display_img(img, filter):
    plt.figure(figsize=(12,8))
    plt.imshow(img)
    plt.title(f'Image with {filter}')
    if filter == "":
        plt.title(f'Image with {filter}')
    plt.axis("off")
    plt.show()



def save_img(image, new_image):
    save = input("Would you like to save your image? ").lower().strip()
    if save == "yes" or save == "y":
        save_name = input("Type a custom name for your file: ").strip()
        bad_charac = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "."]
        for i in bad_charac:
            if i in save_name:
                print("That is an invalid name.\n")
                return
        if save_name in images:
            print("There is a file that already exists with that name.\n")
            return
        ext = os.path.splitext(image)[1]
        save_name2 = "Images/" + save_name + ext
        cv2.imwrite(save_name2, new_image)
        print("Image saved. \n")       
    else:
        print("Image not saved.\n")



def cv2_filter(image):
    img = cv2.imread(image)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img_gray, cmap="gray")
    plt.title(f"{image} in Gray")
    plt.show()

    cropped_img = img_gray[200:300, 300:500]
    plt.imshow(cropped_img, cmap="gray")
    plt.title(f"{image} in Gray and Crop")
    plt.show()

    w, h = cropped_img.shape
    center = w // 2, h // 2
    img_matrix = cv2.getRotationMatrix2D(center, 70, 1)
    rotated_img = cv2.warpAffine(cropped_img, img_matrix, (w, h))
    plt.imshow(rotated_img)
    plt.title(f"{image} Rotated and Crop")
    plt.show()

    brightness_matrix = np.ones(rotated_img.shape, dtype="uint8") * 50
    brightness_img = cv2.add(rotated_img, brightness_matrix)
    plt.imshow(brightness_img, cmap="gray")
    plt.title(f"{image} Rotated and Crop with Brightness Increased")
    plt.show()

    cv2.imwrite(f"Images/gray_image.jpg", img_gray)
    cv2.imwrite(f"Images/cropped_image.jpg", cropped_img)
    cv2.imwrite(f"Images/warped_image.jpg", rotated_img)
    cv2.imwrite(f"Images/brightness_image.jpg", brightness_img)



def user_interaction():
    print("\nWelcome to Image Changing.")

    while True: 
        print("\nTo get started, chose an image:\n")
        image_path = ("Images")
        for i, path in enumerate(os.listdir(image_path), start=1):
            print(f"{i}. {path}")
            images.append(path)

        image_choice = int(input("\nChoose the number that corresponds to that image\n (Please close the window that appears on your screen to continue the aplication): ")) - 1

        if image_choice > len(images)-1:
            print("That is an invalid option. Please try again.\n")
        else:
            display(images[image_choice], "Images/"+images[image_choice])
            print("\nThe image that you chose should have shown up on your screen.\n")
            cv2_filter("Images/"+images[image_choice])
            


if __name__ == "__main__":
    user_interaction() 