# Doppel Demo 

<i> Note: This is a fictional case study. All references to companies and movies are for our imaginary use case, though they are actual brands.</i> 

<img src="https://github.com/MIAISEMAN/mod4_project/master/website_photos/logo_mlw.png", width="50%" height="50%">

At MLW Studios, we drive consumer engagement through consumer experiences. Here we present our prototype to Universal Pictures for the premiere of their movie "Hobbs and Shaw: A Fast and Furious Film" Will use Doppel to increase brand awareness through potential customer experiences.# Goal: Increase consumer engagement and brand awareness with the Doppel product, which allows consumers to instantly compare themselves to characters represented by your brand. 


# Business Need
## Brand Awareness 
Typically, the release of a Fast & Furious film is met with eager anticipation from fans. Based on the digital footprint alone, as seen below in the Google Search History since 2011, this is not the case for Fast & Furious Presents Hobbs & Shaw:
<img src="https://github.com/MIAISEMAN/mod4_project/master/website_photos/graph.png", width="100%" height="100%", align="">

## Consumer Engagement 
Consumers are incredibly loyal to the Fast & Furious brand, but in the case of Hobbs & Shaw, they may be unaware that the movie exists or is related to the franchise. You need a fun way for them to be reminded of the franchise. 

## A Doppel Do Ya!
With the Doppel app, consumers instantly see their celebrity doppelgänger! The app can be customized to whatever domain of characters you desire. Universal Pictures has ordered the Fast & Furious Doppel to increase brand awareness and consumer engagement before the release of Hobbs & Shaw. 

# Data Understanding 
Our app requires thousands of photographs of the characters' faces in order to produce a doppelgänger. For the demo, we downloaded these images ourselves through public searches. However, in typical deals, these assets will be provided to MLW Studios. The photos don't need to be a specific size, and the more photos the better. For movies, frame grabs would be helpful.  

# Data Preparation
First, we decided on the number of characters that we would include in our output options. We used focus groups to narrow down the long list to 18 beloved and well-known characters.

Next, we used the code at <a href="https://github.com/hardikvasa/google-images-download">this GitHub repo </a> to download hundreds of images per character. 

We stored the images in an AWS s3 bucket, during which we learned a lot about the bucket policy requirements. We culled the images, making sure of their quality - removing any other characters in the photo. 

# Modeling - needs more information!
Using a convolutional neural network that was pretrained on facial recognition.  

# Deployment 
Doppel is deployable as an experiential in-person activation at an event, or it's available for placement on digital properties such as a mobile app or on a website. You can brand the output and allow for sharing on social media sites - when it comes to going viral, a Doppel do ya!   
   

