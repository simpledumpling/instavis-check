import streamlit as st
import numpy as np

from keras import models
from keras.preprocessing.image import img_to_array

from PIL import Image
from concat import concat_imgs

DATA_DIR = 'att_resnet_best_weights.34-0.5114'


def main():
    st.title('InstaVis Checker')

    st.subheader('Are you a guru of creativity or just another guy with boring photos?')
    st.subheader('Let\'s find out!')
    uploaded_files = st.file_uploader("Upload 9 images from your Instagram profile",
                                      type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    err = st.text(' ')

    if len(uploaded_files) > 0:
        if len(uploaded_files) != 9:
            err.text('You should upload 9 images in following formats: jpg, jpeg or png')
        else:
            err.text(' ')
            uploaded_imgs = []
            for uploaded_file in uploaded_files:
                uploaded_imgs.append(Image.open(uploaded_file))
            print(uploaded_imgs)
            merged_img = concat_imgs(uploaded_imgs)
            st.subheader("That's how potential subscribers see your content")
            st.image(merged_img, channels="RGB")

    submit = st.button('Am I a genius creator?')

    if submit:
        st.text("A few seconds, please, and we'll find out!")
        class_lbl = predict(merged_img)

        if class_lbl == 8:  # good_food category was predicted
            st.subheader('This is incredibly delicious food. Good job! We are confident you will be successful! ❤️')

        elif class_lbl == 7:  # bad_food category was predicted
            st.subheader(
                'We can see that you have tried, but do not stop!💪 You can show yours food much more appetizing!')
            st.subheader('Check out some examples for inspiration ❤️')
            st.text('We are sure that you will succeed and and many new subscribers!')

        elif class_lbl == 5:  # good_brand category was predicted
            st.subheader(
                'Even big brands can envy your visuals. Good job! We are confident that you will be successful!❤️')

        elif class_lbl == 4 or class_lbl == 6:  # bad_brand or bad_beauty_services category were predicted
            st.subheader('You can do better!💪')
            st.text('On social networks, we can\'t touch the goods, so we have to trust our eyes.')
            st.text('Try to show your potential customers your product from different angles.')
            st.subheader('Check out some examples for inspiration ❤️')
            st.text('We are sure that you will succeed and new clients will not keep you waiting!')

        elif class_lbl == 0:  # bad_thematic category was predicted
            st.subheader('You can do better!💪')
            st.text('The quality of your content is equal to the quality of your services.')
            st.text('Try to make your content more diverse')
            st.subheader('Check out some examples for inspiration ❤️')
            st.text('We are sure that you will succeed and and many new subscribers!')

        elif class_lbl == 1:  # good_thematic category was predicted
            st.subheader('You have a good thematic blog that can successfully compete with market leaders!❤️')

        elif class_lbl == 3:  # good_lifestyle category was predicted
            st.subheader(
                'We are delighted! You are a visual guru and perfectly combine objects and colors in the photo!❤️')

        elif class_lbl == 2:  # bad_lifestyle category was predicted
            st.subheader('You can do better!💪')
            st.text('Sorry, but your content seems a little boring and monotonous 🥱')
            st.text('Try to limit the range of colors, add a variety of objects to the photo,')
            st.text('and experiment with the angle. An unusual approach can lead you to success!')
            st.subheader('Check out some examples for inspiration ❤️')
            st.text('We are sure that you will succeed and and many new subscribers!')

        st.subheader('Loading another examples for your inspiration')

        if class_lbl == 0 or class_lbl == 1:
            st.write('Great! Uploading good thematic blog example for you...')
            best_merge = Image.open('good_examples/good_thematic.jpg')
            best_merge = best_merge.resize((500, 500))
            st.image(best_merge, channels="RGB")
        elif class_lbl == 2 or class_lbl == 3:
            st.write('Great! Uploading good lifestyle blog example for you...')
            best_merge = Image.open('good_examples/good_lifestyle.jpg')
            best_merge = best_merge.resize((500, 500))
            st.image(best_merge, channels="RGB")
        elif class_lbl == 4 or class_lbl == 5 or class_lbl == 6:
            st.write('Great! Uploading good commercial blog example for you...')
            best_merge = Image.open('good_examples/good_commerce.jpg')
            best_merge = best_merge.resize((500, 500))
            st.image(best_merge, channels="RGB")
        else:
            st.write('Great! Uploading good food blog example for you...')
            best_merge = Image.open('good_examples/good_food.jpg')
            best_merge = best_merge.resize((500, 500))
            st.image(best_merge, channels="RGB")


@st.cache
def predict(merged_img: object) -> int:
    img = prepare_img(merged_img)
    model = load_model(DATA_DIR)
    prediction = model.predict(img)
    return np.argmax(prediction[0])


@st.cache(allow_output_mutation=True)
def load_model(model_path: str):
    model = models.load_model(model_path)
    return model


def prepare_img(img):
    img = img.resize((160, 160))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.
    return img


if __name__ == "__main__":
    main()