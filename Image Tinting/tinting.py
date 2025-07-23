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
    print("Choose a filter for your chosen image:")
    print("\n 'r' - apply red tint\n 'g' - apply green tint\n 'b' - apply blue tint\n 'i' - increase red tint intensity\n 'd' - decrease red tint intensity\n 'y' - increase green tint intensity\n 'p' - decrease green tint intensity\n 'j' - increase blue tint intensity\n 'k' - decrease blue tint intensity\n 'q' - go back")
    
    while True:
        choice = input("\nType the corresponding key of your choice\n (Please close the window that appears on your screen to continue the aplication): ")

        if choice == "r":
            copy = img.copy()
            copy[:, :, 1] = 0
            copy[:, :, 2] = 0
            display_img(copy, "Red Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "g":
            copy = img.copy()
            copy[:, :, 0] = 0
            copy[:, :, 2] = 0
            display_img(copy, "Green Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "b":
            copy = img.copy()
            copy[:, :, 0] = 0
            copy[:, :, 1] = 0
            display_img(copy, "Blue Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "i":
            copy = img.copy()
            copy[:, :, 0] = cv2.add(img[:,:,0], 50)
            display_img(copy, "Increased Red Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "d":
            copy = img.copy()
            copy[:, :, 0] = cv2.subtract(img[:,:,0], 50)
            display_img(copy, "Decreased Red Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "y":
            copy = img.copy()
            copy[:, :, 1] = cv2.add(img[:,:,1], 50)
            display_img(copy, "Increased Green Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "p":
            copy = img.copy()
            copy[:, :, 1] = cv2.subtract(img[:,:,1], 50)
            display_img(copy, "Decreased Green Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "j":
            copy = img.copy()
            copy[:, :, 2] = cv2.add(img[:,:,2], 50)
            display_img(copy, "Increased Blue Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "k":
            copy = img.copy()
            copy[:, :, 2] = cv2.subtract(img[:,:,2], 50)
            display_img(copy, "Decreased Blue Tint")
            print("\nThe image should have hown up on your screen.\n")
            save_img(image, copy)
        elif choice == "q":
            break
        else:
            print("That is an invalid option. Please try again.\n")


def user_interaction():
    print("\nWelcome to Computer Vision 2 Tinting.")

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