import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests

st.set_page_config(layout="wide", page_title="Anushka Dhekne - Portfolio")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"File not found: {file_name}")

local_css("style/style.css")

# Load Lottie animations
lottie_coder = load_lottie_url("https://lottie.host/afd583c5-73f7-482b-bb88-3f2f6a191e23/tcD4ZQYG6i.json")
lottie_contact = load_lottie_url("https://lottie.host/7a6810d9-5b60-4327-85ec-f51d974c2286/R57NMxqlgY.json")

#image1 = Image.open("Images/april.png")
image_resume_thumbnail = Image.open("Images/resume_thumbnail.png")
pdf_path = "Images/AnushkaDhekne__Resume.pdf"

# Images for certifications
image1 = "Images/AutomationPro-I.png"
image2 = "Images/AutomationPro-II.png"
image3 = "Images/AWS_DevOps.png"
image4 = "Images/Google_BERT.png"
image5 = "Images/IBM_DataAnalysis.png"
image6 = "Images/Microsoft_Azure.png"
image7 = "Images/OCI_Cloud_Data_Management.png"
image8 = "Images/OCI_Cloud_Infrastructure_Associate.png"
image9 = "Images/OCI_GenAI.png"
image10 = "Images/Udemy_Golang.png"
#image_anushka = "Images/Anushka.jpg"

# Initialize session state for contact form submission
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Left Panel for Navigation
with st.sidebar:
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #F5F5F5; /* Light Gray */
            color: #333; /* Dark Gray */
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .sidebar .sidebar-content a {
            text-decoration: none;
            color: #333;
        }
        .sidebar .sidebar-content .nav-link {
            display: flex;
            align-items: center;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            color: #333;
            font-size: 0.9rem; /* Smaller font size */
            font-weight: 500;
        }
        .sidebar .sidebar-content .nav-link:hover {
            background-color: #E0E0E0; /* Light Gray */
        }
        .sidebar .sidebar-content .nav-link.active {
            background-color: #B3E5FC; /* Light Blue */
            color: #0277BD; /* Darker Blue */
            font-weight: bold;
        }
        .sidebar .sidebar-content .nav-link i {
            margin-right: 0.5rem;
        }
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #555;
        }
        .footer img {
            border-radius: 50%;
            width: 80px;
            height: 80px;
            object-fit: cover;
        }
        </style>
        """, unsafe_allow_html=True
    )

    selected_main = option_menu(
        menu_title="Main Menu",
        options=["Info", "Projects", "Skills & Achievements", "Contact Me"],
        icons=["info-circle", "folder","star", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#F5F5F5"},
            "icon": {"color": "#333", "font-size": "1.2rem"},
            "nav-link": {"font-size": "0.9rem", "text-align": "left", "padding": "0.5rem 1rem"},
            "nav-link-selected": {"background-color": "#B3E5FC"},
        }
    )

    if selected_main == "Info":
        selected_info = option_menu(
            menu_title="Info",
            options=["About", "Resume"],
            icons=["person", "file-earmark-text"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#F5F5F5"},
                "icon": {"color": "#333", "font-size": "1.2rem"},
                "nav-link": {"font-size": "0.9rem", "text-align": "left", "padding": "0.5rem 1rem"},
                "nav-link-selected": {"background-color": "#B3E5FC"},
            }
        )

    elif selected_main == "Projects":
        selected_projects = option_menu(
            menu_title="Projects",
            options=[
                "Resume Matching System",
                "YouTube Trending Videos Analysis",
                "Stock Price Prediction",
                "Commonsense QA Model",
                "Client Server Token Manager",
                "Encrypted File System",
                "Information Retrieval System",
                "Blog Generator",
                "NER Tagging Application",
                "MCQ Generator"
            ],
            #icons=["file-code"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#F5F5F5"},
                #"icon": {"color": "#333", "font-size": "1.2rem"},
                "nav-link": {"font-size": "0.9rem", "text-align": "left", "padding": "0.5rem 1rem"},
                "nav-link-selected": {"background-color": "#B3E5FC"},
            }
        )


    elif selected_main == "Skills & Achievements":
        selected_skills = option_menu(
            menu_title="Skills & Achievements",
            options=["Skills", "Achievements"],
            icons=["star", "award"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#F5F5F5"},
                "icon": {"color": "#333", "font-size": "1.2rem"},
                "nav-link": {"font-size": "0.9rem", "text-align": "left", "padding": "0.5rem 1rem"},
                "nav-link-selected": {"background-color": "#B3E5FC"},
            }
        )
        
        
    # Footer section
    st.write("##")
    st.write("##")
    st.sidebar.markdown("""
        <div class="footer" style="text-align: center; font-size: 12px; color: #555555;">
            <div>Made with ❤️ by Anushka</div>
        </div>
    """, unsafe_allow_html=True)
    
    
# Main content based on sidebar selection
if selected_main == "Info":
    if selected_info == "About":
        col1, col2 = st.columns([2, 1])
        with col1:
            st.title("Hi! I am Anushka Dhekne 👋")
            st.subheader("Master of Science - Computer Science")
            st.write("""
                Results-driven Software Developer and Data Science enthusiast skilled in Python, AWS, and cloud technologies, with expertise in ML, NLP, and data integration. Proven ability to deliver impactful, scalable solutions through technical excellence and collaborative problem-solving.
                My expertise lies in Machine Learning, Data Analytics, and Web Development. I love exploring new technologies and applying them to real-world problems.
            """)
    
            st.markdown("""
                <div style="display: flex; gap: 10px;">
                    <a href="https://www.linkedin.com/in/anushka-dhekne" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="30">
                    </a>
                    <a href="https://github.com/dAnushka77" target="_blank">
                        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" height="30">
                    </a>
                </div>
            """, unsafe_allow_html=True)
        
        
        with col2:
            st_lottie(lottie_coder, height=200)  # Increased size for GIF

        st.write('---')

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.markdown("""
                - <p style="text-decoration: underline;">University of Maryland, Baltimore County (USA)</p>
                    - Master of Science - Computer Science<br>
                    - August 2022 - May 2024<br>
                    - GPA: 3.6/4.0
                ##
                - <p style="text-decoration: underline;">Savitribai Phule Pune University (India)</p>
                    - Bachelor of Engineering - Computer Engineering<br>
                    - June 2016 - May 2020<br>
                    - GPA: 3.6/4.0
            """, unsafe_allow_html=True)
        with col4:
            st.subheader("Professional Experience")
            st.markdown("""
                - <p style="text-decoration: underline;">Cerebrone.ai (Cloud Intern) | August 2023 - December 2023</p>
                    - Managed AWS EC2 and Linux.<br>
                    - Designed scalable Edge AI solutions.<br>
                ##
                - <p style="text-decoration: underline;">Harbinger Group (Software Engineer) | July 2020 - July 2022</p>
                    - Developed 93% accurate brain analysis.<br>
                    - Built 85% accurate sentiment model.<br>
                    - Improved QA efficiency by 30%.<br>
                    - Reduced diagnostic errors by 25%.<br>
                    - Enhanced job matching by 20%.<br>
                ##
                - <p style="text-decoration: underline;">Indicus Softwares Pvt. Ltd. (Software Engineering Intern) | September 2019 - April 2020</p>
                    - Developed vehicle pooling app.<br>
                    - Integrated Geofence, Google Maps API.<br>
            """, unsafe_allow_html=True)

    elif selected_info == "Resume":
        st.header("View My Resume")
        st.write("##")
        col7 = st.columns(1)
        with col7[0]:
            # Display the thumbnail image without making it clickable
            st.image(image_resume_thumbnail, use_column_width=False, width=400)
            st.write("##")

            # Provide a download link for the PDF
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="Download My Resume",
                    data=pdf_file,
                    file_name="AnushkaDhekne_Resume.pdf",
                    mime="application/pdf"
                )



elif selected_main == "Projects":
    
    if selected_projects == "Resume Matching System":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Resume Matching System</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Job_Description_and_Resume_Matching_System" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Created a resume matching system using Python, Flask, NLP, SpaCy, TfIDF, and Scikit-Learn. This system matches resumes with job descriptions based on key skills and experience, improving the recruitment process by 30%.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul class="project-description">
                        <li>Python</li>
                        <li>Flask</li>
                        <li>NLP</li>
                        <li>SpaCy</li>
                        <li>TfIDF</li>
                        <li>Scikit-Learn</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)


    elif selected_projects == "YouTube Trending Videos Analysis":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">YouTube Trending Videos Analysis</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/YouTube-Trending-Videos-Analysis" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Analyzed trending YouTube videos using Python, Pandas, and Matplotlib. Extracted insights on trending topics, viewership patterns, and content creators' strategies.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul class="project-description">
                        <li>Python</li>
                        <li>Pandas</li>
                        <li>Matplotlib</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)      


    elif selected_projects == "Stock Price Prediction":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Stock Price Prediction</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Financial_Data_Science__Stock_Prediction" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Developed a stock price prediction model using LSTM neural networks, achieving 87% accuracy in predicting stock prices for technology companies.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>LSTM Neural Networks</li>
                        <li>Python</li>
                        <li>TensorFlow</li>
                        <li>Keras</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)        

    elif selected_projects == "Commonsense QA Model":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Commonsense QA Model</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Commonsense-QA" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Built a commonsense question-answering model using BERT, achieving a significant improvement in answering accuracy by incorporating contextual understanding.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>BERT</li>
                        <li>Python</li>
                        <li>TensorFlow</li>
                        <li>Hugging Face Transformers</li>
                    </ul>
                </div>
            </div>
        </div>

        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        

    elif selected_projects == "Client Server Token Manager":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Client Server Token Manager</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Token-Management-in-Go" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Developed a client-server token management system using Go, ensuring secure and efficient token handling for various applications.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Go</li>
                        <li>REST API</li>
                        <li>JWT</li>
                    </ul>
                </div>
            </div>
        </div>

        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        

    elif selected_projects == "Encrypted File System":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Encrypted File System</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Enhanced-Distributed-File-System" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Developed an encrypted file system using Python and AES encryption, providing secure file storage and access control for sensitive data.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>AES Encryption</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        
        

    elif selected_projects == "Information Retrieval System":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Information Retrieval System</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Information-Retrieval" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Created an information retrieval system using Python, NLP, and BM25 algorithm to efficiently search and retrieve relevant documents from large datasets.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>NLP</li>
                        <li>BM25 Algorithm</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        
        

    elif selected_projects == "Blog Generator":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Blog Generator</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/Llama2_Blog_Generator" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Developed an automated blog generator using Python, NLP, and GPT-3, enabling users to generate high-quality blog posts based on specific topics and keywords.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>NLP</li>
                        <li>GPT-3</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        

    elif selected_projects == "NER Tagging Application":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">NER Tagging Application</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/NER_Application" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Built a Named Entity Recognition (NER) tagging application using Python, SpaCy, and Flask, allowing users to tag and categorize entities within large text datasets.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>SpaCy</li>
                        <li>Flask</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        

    elif selected_projects == "MCQ Generator":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">MCQ Generator</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/MCQ_Generator" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Created an MCQ generator using Python and Flask, which generates multiple-choice questions from a given dataset and allows users to customize question parameters.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>Flask</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)
        

    elif selected_projects == "NLP Sentiment Analyzer":
        st.markdown('''
        <div class="project-box">
            <h2 class="project-title">Sentiment Analyzer</h2>
            <div class="flex-container" style="margin-top: 20px;">
                <div style="flex: 1; min-width: 200px; margin-right: 20px;">
                    <div id="project-image"></div>
                </div>
                <div style="flex: 2; min-width: 250px;">
                    <a href="https://github.com/dAnushka77/NLP_Sentiment_Analyzer_Model" style="font-weight: bold; color: #4682b4; text-decoration: none; display: block; margin-bottom: 10px;"><span style="font-size: 20px; margin-right: 8px;">💡</span>GitHub Link</a>
                    <p class="project-description">
                        Developed a sentiment analysis model using Python and NLP techniques, providing insights into the sentiment and emotional tone of textual data.
                    </p>
                    <p class="project-description" style="font-weight: bold;">Tech Stack Used:</p>
                    <ul style="font-size: 16px; color: #333;">
                        <li>Python</li>
                        <li>NLP</li>
                    </ul>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        # Display the image using Streamlit
        #st.image(image1, width=200, use_column_width='never', caption=None)


elif selected_main == "Skills & Achievements":
    if selected_skills == "Skills":
        st.title("Skills")
        # Programming Languages
        st.subheader("Programming Languages")
        st.markdown("""
        <div style="display: flex; flex-direction: row; gap: 10px;">
            <div style="border: 2px solid #6B5B95; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/c-programming.png" height="30"/>
                <span style="margin-left: 5px;">C</span>
            </div>
            <div style="border: 2px solid #6B5B95; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/c-plus-plus-logo.png" height="30"/>
                <span style="margin-left: 5px;">C++</span>
            </div>
            <div style="border: 2px solid #306998; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/python.png" height="30"/>
                <span style="margin-left: 5px;">Python</span>
            </div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">R</div>
            <div style="border: 2px solid #6B5B95; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/ios-filled/50/000000/mysql-logo.png" height="30"/>
                <span style="margin-left: 5px;">MySQL</span>
            </div>
            <div style="border: 2px solid #6B5B95; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/java-coffee-cup-logo.png" height="30"/>
                <span style="margin-left: 5px;">Java</span>
            </div>
            <div style="border: 2px solid #F7DF1E; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/javascript.png" height="30"/>
                <span style="margin-left: 5px;">JavaScript</span>
            </div>
            <div style="border: 2px solid #00ADD8; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/golang.png" height="30"/>
                <span style="margin-left: 5px;">Golang</span>
            </div>
            <div style="border: 2px solid #E44D26; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/html-5--v1.png" height="30"/>
                <span style="margin-left: 5px;">HTML</span>
            </div>
            <div style="border: 2px solid #1572B6; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/css3.png" height="30"/>
                <span style="margin-left: 5px;">CSS</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("##")
        # Frameworks
        st.subheader("Frameworks")
        st.markdown("""
        <div style="display: flex; flex-direction: row; gap: 10px;">
            <div style="border: 2px solid #000000; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/flask.png" height="30"/>
                <span style="margin-left: 5px;">Flask</span>
            </div>
            <div style="border: 2px solid #092E20; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/django.png" height="30"/>
                <span style="margin-left: 5px;">Django</span>
            </div>
            <div style="border: 2px solid #61DAFB; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/react-native.png" height="30"/>
                <span style="margin-left: 5px;">React</span>
            </div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">FastAPI</div>
            <div style="border: 2px solid #FF6F61; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/tensorflow.png" height="30"/>
                <span style="margin-left: 5px;">TensorFlow</span>
            </div>
            <div style="background-color: #6B5B95; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">PyTorch</div>
            <div style="background-color: #88B04B; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Spark</div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Agile</div>
            <div style="background-color: #FF6F61; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">SAS</div>
            <div style="border: 2px solid #563D7C; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/bootstrap.png" height="30"/>
                <span style="margin-left: 5px;">Bootstrap</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("##")
        # Tools
        st.subheader("Tools")
        st.markdown("""
        <div style="display: flex; flex-direction: row; gap: 10px;">
            <div style="border: 2px solid #F05032; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/git.png" height="30"/>
                <span style="margin-left: 5px;">Git</span>
            </div>
            <div style="border: 2px solid #F7DF1E; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/json.png" height="30"/>
                <span style="margin-left: 5px;">JSON</span>
            </div>
            <div style="border: 2px solid #0DB7ED; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/docker.png" height="30"/>
                <span style="margin-left: 5px;">Docker</span>
            </div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Postman</div>
            <div style="border: 2px solid #D0B400; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/power-bi.png" height="30"/>
                <span style="margin-left: 5px;">PowerBI</span>
            </div>
            <div style="border: 2px solid #E9E9E9; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/tableau-software.png" height="30"/>
                <span style="margin-left: 5px;">Tableau</span>
            </div>
            <div style="background-color: #88B04B; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">ETL</div>
            <div style="border: 2px solid #F24E1E; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/figma.png" height="30"/>
                <span style="margin-left: 5px;">FIGMA</span>
            </div>
            <div style="background-color: #FF6F61; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Google Charts</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("##")
        # Methodologies
        st.subheader("Methodologies")
        st.markdown("""
        <div style="display: flex; flex-direction: row; gap: 10px;">
            <div style="background-color: #FF6F61; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">CI/CD</div>
            <div style="background-color: #6B5B95; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">OOP</div>
            <div style="background-color: #88B04B; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">REST</div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Data Analytics</div>
            <div style="background-color: #FF6F61; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Machine Learning</div>
            <div style="background-color: #6B5B95; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">NLP</div>
            <div style="background-color: #88B04B; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">Prompt Engineering</div>
            <div style="background-color: #FFA500; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">DevOps</div>
         </div>
        """, unsafe_allow_html=True)
        st.write("##")
        # Platforms/Databases
        st.subheader("Platforms/Databases")
        st.markdown("""
        <div style="display: flex; flex-direction: row; gap: 10px;">
            <div style="background-color: #FF6F61; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">AWS</div>
            <div style="border: 2px solid #000000; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/linux.png" height="30"/>
                <span style="margin-left: 5px;">Linux</span>
            </div>
            <div style="background-color: #88B04B; padding: 10px 15px; border-radius: 5px; color: white; font-weight: bold;">GCP</div>
            <div style="border: 2px solid #326CE5; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/kubernetes.png" height="30"/>
                <span style="margin-left: 5px;">Kubernetes</span>
            </div>
            <div style="border: 2px solid #0DB7ED; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/docker.png" height="30"/>
                <span style="margin-left: 5px;">Docker</span>
            </div>
            <div style="border: 2px solid #F80000; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/oracle-logo.png" height="30"/>
                <span style="margin-left: 5px;">Oracle</span>
            </div>
            <div style="border: 2px solid #4DB33D; border-radius: 5px; padding: 5px 10px; display: flex; align-items: center;">
                <img src="https://img.icons8.com/color/48/000000/mongodb.png" height="30"/>
                <span style="margin-left: 5px;">MongoDB</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


    elif selected_skills == "Achievements":
        st.title("Achievements")
        
        st.markdown("""
        - Received the Harbinger Superstar of the Month Award in October 2020.
        - Participated in the Code Review Bugathon.
        """)     
        st.write("##")
        st.subheader("Certifications")
        
        # Display images with larger captions using markdown
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(image6, caption="Microsoft AI on Azure", use_column_width=True)
            st.image(image3, caption="AWS DevOps", use_column_width=True)
            st.image(image4, caption="Google Cloud Transformer & BERT", use_column_width=True)

        with col2:
            st.image(image5, caption="IBM Data Analysis using Python", use_column_width=True)
            st.image(image1, caption="Workato Automation Pro I", use_column_width=True)
            st.image(image2, caption="Workato Automation Pro II", use_column_width=True)
            st.image(image10, caption="Udemy Golang", use_column_width=True)

        with col3:
            st.image(image8, caption="OCI Foundations Associate", use_column_width=True)
            st.image(image9, caption="Oracle Gen AI Professional", use_column_width=True)
            st.image(image7, caption="Oracle Cloud Data Management", use_column_width=True)

        # Apply custom CSS for larger captions
        st.markdown(
            """
            <style>
            .stImage img {
                max-width: 100%;
            }
            .stImage .caption {
                font-size: 1.2rem;  /* Increase caption size */
                text-align: center;  /* Center the caption */
            }
            </style>
            """,
            unsafe_allow_html=True
        )


elif selected_main == "Contact Me":
    # Center and resize the Lottie animation along with the header
    st.markdown("""
    <style>
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px; /* Adjust gap between header and animation */
        margin-top: 20px;
    }

    .lottie-animation {
        height: 70px; /* Adjust height of the Lottie animation */
        width: 70px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.header(":mailbox: Get In Touch With Me!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st_lottie(lottie_contact, height=110, width=110, key="contact-animation")  # Resize Lottie animation

    # Contact Form
    contact_form = """
    <form action="https://formsubmit.co/anushkadhekne@gmail.com" method="POST" onsubmit="handleFormSubmit(event)">
         <input type="hidden" name="_captcha" value="false">
         <input type="hidden" name="_next" value="https://myportfolio-anu7shkadhekne7.streamlit.app/"> <!-- Redirect URL after submission -->
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit" class="send-button">Send</button>
    </form>
    <script>
    function handleFormSubmit(event) {
        event.preventDefault(); // Prevent the default form submission
        // Display the notification
        alert("Thank you for reaching out! Your message has been sent.");
        // Use setTimeout to ensure the alert is displayed before form submission
        setTimeout(function() {
            event.target.submit(); // Submit the form after showing the notification
        }, 50); // Adjust the delay if necessary
    }
    </script>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    st.write("##")

    # Custom CSS for the form and button
    st.markdown("""
    <style>
    form {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    input, textarea {
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
        border: 1px solid #ddd;
        width: 100%;
    }

    textarea {
        height: 150px;
        resize: vertical;
    }

    .send-button {
        padding: 12px;
        background: linear-gradient(45deg, #28a745, #218838); /* Gradient background */
        color: white;
        font-size: 16px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.3s ease, background 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .send-button:hover {
        background: linear-gradient(45deg, #218838, #28a745);
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .send-button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
