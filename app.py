import streamlit as st
from PIL import Image
from main import img2text, story_generator
from streamlit_lottie import st_lottie
import json

def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url
    
def main():
    st.set_page_config(page_title="Moral StoryTeller", page_icon="🤖")
    st.title("Moral StoryTeller 🤖📚")
    data_oracle = import_json(r"roboreads.json")
    st_lottie(data_oracle, height = 400, key = "oracle")
    st.header("Let's Turn Images into Stories!")
    #horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"
    with st.sidebar:
        #st.subheader("Moral Storyteller🤖📚")
        #st.markdown(horizontal_bar, True)

        # sidebarlogo = Image.open('sidebarlogo.jpg').resize((300, 420))
        sidebarlogo = Image.open('robocute.png').resize((300, 390))
        st.image(sidebarlogo, use_column_width='True')
    
    st.sidebar.success("""Welcome to our AI Moral Storyteller! 📚✨

Our Moral Storyteller is an innovative project that harnesses the power of artificial intelligence to craft engaging and thought-provoking moral stories from a series of images. 
As you embark on your journey through our stories, you'll encounter tales woven with wisdom, empathy, and lessons that resonate with both young and old alike. Each story is carefully crafted to inspire introspection, empathy, and positive values.
Let's venture into a journey of discovery, enlightenment, and moral reflection together!
Happy storytelling! 🌟""")

    # Define sidebars
    #left_sidebar = st.sidebar
    #right_sidebar = st.sidebar

    # Left sidebar
    #left_sidebar.image(Image.open("robo.png"), width=200)

    # Main content area
    main_content = st

    # Middle content
    upload_files = main_content.file_uploader(" ", type='jpg', accept_multiple_files=True)  # Uploads images
    st.info("Please upload three images to get started.")
    if upload_files:
        if len(upload_files) == 3:
            binary_data_1 = upload_files[0].getvalue()
            binary_data_2 = upload_files[1].getvalue()
            binary_data_3 = upload_files[2].getvalue()
            
            with open(upload_files[0].name, 'wb') as f:
                f.write(binary_data_1)
            with open(upload_files[1].name, 'wb') as f:
                f.write(binary_data_2)
            with open(upload_files[2].name, 'wb') as f:
                f.write(binary_data_3)
            
            # Display images in three columns
            col1, col2, col3 = st.columns(3)
            scenario_1 = img2text(upload_files[0].name)  # Text to image for image 1
            scenario_2 = img2text(upload_files[1].name)  # Text to image for image 2
            scenario_3 = img2text(upload_files[2].name)

            with col1:
                st.image(Image.open(upload_files[0]), caption=scenario_1, width=200)
            with col2:
                st.image(Image.open(upload_files[1]), caption=scenario_2, width=200)
            with col3:
                st.image(Image.open(upload_files[2]), caption=scenario_3, width=200)

            
            
            # Generate captions for all three images
            caption = story_generator(scenario_1, scenario_2, scenario_3)

            # Combine captions into a single story
            story = f"{caption}"

            # Display combined story
            with main_content.expander("Here's your Moral Story"):
                main_content.write(story)
        else:
            st.error("Please upload exactly three images to continue.")

    # Right sidebar
    #right_sidebar.image(Image.open("robocute.png"), width=200)

    # Footer Section
    st.markdown("---")
    col1 = st.columns(1)
    with col1[0]:
        st.image(Image.open("kid.png"), width=100)
        st.write("Hope you enjoy the stories :)")
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.markdown("<p style='color:grey;'>Moral Storyteller web app is designed for entertainment and educational purposes only.</p>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.markdown('<p style="font-size:12px; color:#808080;">©2024 FinalYearProject by LISA BOJAMMA MS & JEEVA JALEESH</p>', unsafe_allow_html=True)


# the main
if __name__ == "__main__":
    main()
