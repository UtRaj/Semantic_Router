# Semantic_Router

**This project demonstrates the use of the semantic_router library to classify text into predefined categories or "routes" using a semantic text encoder. The application is built using Gradio to provide an easy-to-use web interface.**

## Overview

**The project uses semantic_router, which employs semantic text encoding to classify text into one of several predefined categories based on the content. The Gradio interface allows users to input a sentence and get the classified route as the output.**

## Project Structure

**semantic_router:** A custom library used to create semantic routes and classify text based on them.

**gradio:** A library that provides an easy way to create a web-based interface for machine learning models.


## Routes Defined

The project at this stage defines five different routes:

**Dessert:** Sentences related to desserts, especially those involving chocolate, whiskey, and pecans.

**Nuts:** Sentences related to pecans and other nuts, often in combination with bourbon.

**Smoke:** Sentences that mention smoking or smoked ingredients, especially in the context of cooking or cocktails.

**Spices:** Sentences that involve spices, particularly cinnamon, ginger, and their combinations with bourbon.

**Fruits:** Sentences that talk about fruits, especially in the context of cocktails and other drinks.


Each route is defined using a Route object that includes a name and a list of utterances.

## Usage

To run this project locally, you need to install the required dependencies. You can do this by running:

### Installing Dependancies

```
pip install gradio semantic_router
```

### Running the Application

You can launch the Gradio interface by running:

```
python app.py
```

This will open a web-based interface where you can enter a sentence and see which route it matches based on the semantic content.

### Example

Once the application is running, you can input sentences like:

1. **"I made a big batch of Pineapple Whiskey Sours for tonight."**

2. **"Curious to see how cinnamon forward it is. I love cinnamon flavor in bourbon."**
   
The interface will classify these inputs into their respective categories.

## Code Explanation

### Defining Routes

Routes are defined using the Route class from the semantic_router library. Each route is identified by a name and a list of utterances that are representative of the content that should be classified under this route.

### Encoding and Classification
The HuggingFaceEncoder is used to encode the input text. The RouteLayer class then uses these encodings to determine which route the input text best matches.

### Gradio Interface
The Gradio interface is defined using gr.Interface, which takes the classification function (classify_text) as its main function. The interface accepts text input and returns the name of the route as output.

## Links

[Semantic Router on Hugging Face](https://huggingface.co/spaces/Rajut/Semantic_router)

