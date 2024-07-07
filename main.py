from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
import requests
import os
import streamlit as st
from nltk.translate.bleu_score import corpus_bleu

load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

#img-to-text

def img2text(path):
    img_to_text = pipeline(
    "image-to-text", model="Salesforce/blip-image-captioning-base")
    text = img_to_text(path)[0]['generated_text']
    return text

def story_generator(scenario_1,scenario_2,scenario_3):
    template = """
    You are an expert kids story teller;
    You can generate moral short stories based on a simple narrative
    Your story should be within 300 words.
    Give the story a title in Bold

    CONTEXT 1: {scenario_1}
    CONTEXT 2: {scenario_2}
    CONTEXT 3: {scenario_3}
    STORY:
    """
    prompt = PromptTemplate(template=template, input_variables=["scenario_1", "scenario_2","scenario_3"])
    story_llm = LLMChain(llm=OpenAI(model_name='gpt-3.5-turbo', temperature=1), prompt=prompt, verbose=True)
    combined_scenario = f"{scenario_1}\n{scenario_2}\n{scenario_3}"
    story = story_llm.predict(scenario_1=scenario_1, scenario_2=scenario_2,scenario_3=scenario_3,combined_scenario=combined_scenario)
    return story

def compute_bleu_score(reference, generated):
    # Convert reference and generated stories to lists of tokens
    reference_tokens = [reference.split()]
    generated_tokens = generated.split()
    # Compute BLEU score
    return corpus_bleu(reference_tokens, [generated_tokens])

reference_story = "In a quiet suburban neighborhood stood a cozy house, where the Smith family resided. One fateful evening, as the sun dipped below the horizon, a spark ignited in the kitchen, quickly engulfing the entire home in flames. Amidst the chaos, a man in a black jacket and white pants happened to be passing by. His name was Jack, a retired firefighter. Without hesitation, he dashed towards the blazing house. Inside, Mr. and Mrs. Smith were frantically searching for their daughter, Emily, who was trapped on the second floor.Meanwhile, the sound of a roaring engine echoed through the street. A red Bull racing car screeched to a halt, and out stepped a young driver named Max. He had been practicing nearby when he noticed the billowing smoke. Despite being in the middle of his training, Max couldn't ignore the cries for help. Jack and Max exchanged a glance, both understanding the urgency of the situation. Together, they devised a plan. Jack would enter the burning house while Max positioned his racing car strategically.With Jack's expertise and Max's quick thinking, they managed to rescue Emily just in time. As they emerged from the inferno, the neighborhood erupted into applause. The Smith family embraced Jack and Max, grateful for their bravery and selflessness.In the aftermath, the community came together to support the Smiths, helping them rebuild their home and their lives. Jack and Max's heroic actions inspired others to look out for their neighbors and lend a helping hand in times of need.The moral of the story is that true heroes come in all forms, from experienced professionals like Jack to unexpected allies like Max. When faced with adversity, it's not just about individual courage but also about teamwork and compassion. And sometimes, the most unlikely partnerships can lead to extraordinary outcomes, proving that even amidst tragedy, there is hope and humanity."
generated_story = "Once upon a time, in a small town, there was a house on fire. The flames were spreading quickly and everyone was in a panic. But amidst the chaos, a brave firefighter in a black jacket and white pants arrived at the scene. He immediately sprung into action, directing his team to extinguish the fire and rescue anyone trapped inside.As the firefighter entered the burning building, he heard cries for help coming from the top floor. Without hesitation, he ran up the stairs and found a family huddled together, unable to escape. With great courage, he led them to safety, risking his own life to save others.After the fire was finally put out, the townspeople gathered around the firefighter in admiration and gratitude. They praised his bravery and selflessness, calling him a hero.The firefighter humbly accepted their thanks but insisted that he was just doing his job. He knew that it was his duty to protect and serve the community, no matter the danger.From that day on, the firefighter became a symbol of hope and courage for the town. Children looked up to him as a role model, inspired to help others in need and always strive to do what is right.And so, the brave firefighter in his black jacket and white pants continued to save lives and make a difference, showing everyone that true heroes are those who put others before themselves."
bleu_score = compute_bleu_score(reference_story, generated_story)
#print("Generated Story:", generated_story)
print("BLEU Score:", bleu_score)
