import cv2
import argparse
import matplotlib.pyplot as plt

def plot_image(image, title='Image', grid=False):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    plt.imshow(image)
    plt.title(title)
    plt.grid(grid)
    plt.show()


if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    args = vars(ap.parse_args())

    img = cv2.imread(args['image'])
    print(img.shape)
    plot_image(img, 'test', True)