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
    unfiltered_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print("Choose a filter for your chosen image:")
    print("\n Edge Detection:\n  1. Sobel\n  2. Canny\n  3. Laplacian\n Noise Reduction:\n  4. Gaussian\n  5. Median Filter\n")
    
    while True:
        choice = input("Choose the number that corresponds to your choice\n (Please close the window that appears on your screen to continue the aplication): ")

        if choice == "1":
            sobelX = cv2.Sobel(unfiltered_img, cv2.CV_64F, 1, 0, ksize=3)
            sobelY = cv2.Sobel(unfiltered_img, cv2.CV_64F, 0, 1, ksize=3)
            sobel_combined = cv2.bitwise_or(sobelX.astype(np.uint8), sobelY.astype(np.uint8))
            display_img(sobel_combined, "Sobel")
            print("\nThe image and filter you chose should have shown up on your screen.\n")
            save_img(image, sobel_combined)
            break
        elif choice == "2":
            lower_thresh = int(input("\nTo apply this filter, you need to declare the lower and upper threshold.\n\nEnter the lower treshold here: "))
            upper_thresh = int(input("Enter the upper treshold here: "))
            if lower_thresh == "" or upper_thresh == "":
                print("Invalid, please try again.\n")
            canny = cv2.Canny(unfiltered_img, lower_thresh, upper_thresh)
            display_img(canny, "Canny")
            print("\nThe image and filter you chose should have shown up on your screen.\n")
            save_img(image, sobel_combined)
            break
        elif choice == "3":
            laplacian = cv2.Laplacian(unfiltered_img, cv2.CV_64F)
            display_img(laplacian, "Laplacian")
            print("\nThe image and filter you chose should have shown up on your screen.\n")
            save_img(image, laplacian)
            break
        elif choice == "4":
            ksize = int(input("\nTo apply this filter, you need to declare an odd kernel size.\n\nEnter an odd kernel size here: "))
            if ksize % 2 == 0:
                print("Your choice is invalid. Please try again.")
                continue
            elif ksize == "":
                print("Invalid, please try again.\n")
            gaussian = cv2.GaussianBlur(unfiltered_img, (ksize, ksize), 0)
            display_img(gaussian, "Gaussian")
            save_img(image, gaussian)
            break
        elif choice == "5":
            ksize2 = int(input("\nTo apply this filter, you need to declare an odd kernel size.\n\nEnter an odd kernel size here: "))
            if ksize2 % 2 == 0:
                print("Your choice is invalid. Please try again.")
                continue
            elif ksize2 == "":
                print("Invalid, please try again.\n")
            median = cv2.medianBlur(unfiltered_img, ksize2)
            display_img(median, "Median")
            save_img(image, median)
            break
        else:
            print("That is an invalid option. Please try again.\n")


def user_interaction():
    print("\nWelcome to Computer Vision 2 Edge Detection and Noise Reduction.")

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
            print(images[image_choice])
            display(images[image_choice], "Images/"+images[image_choice])
            print("\nThe image that you chose should have shown up on your screen.\n")
            cv2_filter("Images/"+images[image_choice])



if __name__ == "__main__":
    user_interaction() 