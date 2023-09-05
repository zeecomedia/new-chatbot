from django.shortcuts import render
from django.http import JsonResponse
import random

import os
import openai


def query_chatgpt_api(new_user_prompt):
    openai.api_key = "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"
    messages=[
        {
        "role": "system",
        "content": "{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"},\n        {\"role\": \"user\", \"content\": \"What are the latest iPhone models?\"},\n        {\"role\": \"assistant\", \"content\": \"The latest iPhone models are the iPhone 13, iPhone 13 mini, iPhone 13 Pro, and iPhone 13 Pro Max.\"},\n        {\"role\": \"user\", \"content\": \"How much does the iPhone 13 Pro Max cost?\"},\n        {\"role\": \"assistant\", \"content\": \"The starting price for the iPhone 13 Pro Max is $1,099 for the base model with 128GB of storage.\"},\n        {\"role\": \"user\", \"content\": \"What are the key features of the iPhone 13 camera?\"},\n        {\"role\": \"assistant\", \"content\": \"The iPhone 13 features an improved dual-camera system with sensor-shift optical image stabilization, Night mode, and Deep Fusion. The Pro models have a triple-camera system with additional capabilities\"},\n        {\"role\": \"user\", \"content\": \"When was the first iPhone released?\"},\n        {\"role\": \"assistant\", \"content\": \"The first iPhone, the iPhone 2G, was released on June 29, 2007.\"},\n        {\"role\": \"user\", \"content\": \"Can I upgrade my current iPhone to iOS 15?\"},\n        {\"role\": \"assistant\", \"content\": \"Whether you can upgrade your current iPhone to iOS 15 depends on the model. iOS 15 supports iPhone 6s and later models.\"},\n        {\"role\": \"user\", \"content\": \"How do I transfer data from my old iPhone to a new one?\"},\n        {\"role\": \"assistant\", \"content\": \"You can transfer data from your old iPhone to a new one using iCloud, iTunes, or the Quick Start feature during the setup process.\"},\n        {\"role\": \"user\", \"content\": \"What is the battery life of the iPhone 13 mini?\"},\n        {\"role\": \"assistant\", \"content\": \"The iPhone 13 mini offers up to 15 hours of talk time or up to 13 hours of internet use on a single charge.\"},\n        {\"role\": \"user\", \"content\": \"Can I use Face ID while wearing a mask?\"},\n        {\"role\": \"assistant\", \"content\": \"Yes, you can use Face ID with a mask on, but you might need to enable 'Face ID with a Mask' in your iPhone's settings for better recognition.\"},\n        {\"role\": \"user\", \"content\": \"Is the iPhone 13 water-resistant?\"},\n        {\"role\": \"assistant\", \"content\": \"Yes, the iPhone 13 is rated as water-resistant with an IP68 rating, which means it can withstand being submerged in water up to a certain depth.\"},\n        {\"role\": \"user\", \"content\": \"What is the storage capacity of the iPhone 13 Pro?\"},\n        {\"role\": \"assistant\", \"content\": \"The iPhone 13 Pro is available in storage capacities of 128GB, 256GB, and 512GB.\"},\n        {\"role\": \"user\", \"content\": \"How can I update my iPhone's operating system?\"},\n        {\"role\": \"assistant\", \"content\": \"You can update your iPhone's operating system by going to 'Settings' > 'General' > 'Software Update' and following the on-screen instructions.\"},\n        {\"role\": \"user\", \"content\": \"Does the iPhone 13 support 5G connectivity?\"},\n        {\"role\": \"assistant\", \"content\": \"Yes, the iPhone 13 supports 5G connectivity for faster data speeds and improved network performance.\"},\n        {\"role\": \"user\", \"content\": \"Can I use wireless charging with the iPhone 13?\"},\n        {\"role\": \"assistant\", \"content\": \"Yes, the iPhone 13 supports wireless charging using Qi-compatible chargers.\"},\n        {\"role\": \"user\", \"content\": \"What colors are available for the iPhone 13 Pro?\"},\n        {\"role\": \"assistant\", \"content\": \"The iPhone 13 Pro is available in colors such as Graphite, Gold, Silver, and Sierra Blue.\"},\n        {\"role\": \"user\", \"content\": \"Does the iPhone 13 have a headphone jack?\"},\n        {\"role\": \"assistant\", \"content\": \"No, the iPhone 13 does not have a headphone jack. It uses a Lightning port or wireless audio options.\"},\n        {\"role\": \"user\", \"content\": \"What is the warranty period for the iPhone 13?\"},\n        {\"role\": \"assistant\", \"content\": \"Most existing iPhone accessories should be compatible with the iPhone 13, but it depends on the specific accessory.\"},\n        {\"role\": \"user\", \"content\": \"Can I use wireless charging with the iPhone 13?\"},\n        {\"role\": \"assistant\", \"content\": \"Yes, the iPhone 13 supports wireless charging using Qi-compatible chargers.\"},\n        {\"role\": \"user\", \"content\": \"How can I contact Apple Support for assistance?\"},\n        {\"role\": \"assistant\", \"content\": \"You can contact Apple Support through the Apple website, Apple Support app, or by calling the Apple Support phone number.\"},\n        {\"role\": \"user\", \"content\": \"Where can I purchase an iPhone 13?\"},\n        {\"role\": \"assistant\", \"content\": \"You can purchase an iPhone 13 from authorized Apple retailers, Apple's official website, or through carrier stores\"},"
        },
        {
        "role": "user",
        "content": "What are the latest iPhone models?"
        },
        {
        "role": "assistant",
        "content": "The latest iPhone models are the iPhone 13, iPhone 13 mini, iPhone 13 Pro, and iPhone 13 Pro Max."
        },
        {
        "role": "user",
        "content": "How much does the iPhone 13 Pro Max cost?"
        },
        {
        "role": "assistant",
        "content": "The starting price for the iPhone 13 Pro Max is $1,099 for the base model with 128GB of storage."
        },
        {
        "role": "user",
        "content": "What are the key features of the iPhone 13 camera?"
        },
        {
        "role": "assistant",
        "content": "The iPhone 13 features an improved dual-camera system with sensor-shift optical image stabilization, Night mode, and Deep Fusion. The Pro models have a triple-camera system with additional capabilities."
        },
        {
        "role": "user",
        "content": "When was the first iPhone released?"
        },
        {
        "role": "assistant",
        "content": "The first iPhone, the iPhone 2G, was released on June 29, 2007."
        },
        {
        "role": "user",
        "content": "Can I upgrade my current iPhone to iOS 15?"
        },
        {
        "role": "assistant",
        "content": "Whether you can upgrade your current iPhone to iOS 15 depends on the model. iOS 15 supports iPhone 6s and later models."
        },
        {
        "role": "user",
        "content": "How do I transfer data from my old iPhone to a new one?"
        },
        {
        "role": "assistant",
        "content": "You can transfer data from your old iPhone to a new one using iCloud, iTunes, or the Quick Start feature during the setup process"
        },
        {
        "role": "user",
        "content": "What is the battery life of the iPhone 13 mini?"
        },
        {
        "role": "assistant",
        "content": "The iPhone 13 mini offers up to 15 hours of talk time or up to 13 hours of internet use on a single charge"
        },
        {
        "role": "user",
        "content": "Can I use Face ID while wearing a mask?"
        },
        {
        "role": "assistant",
        "content": "Yes, you can use Face ID with a mask on, but you might need to enable 'Face ID with a Mask' in your iPhone's settings for better recognition."
        },
        {
        "role": "user",
        "content": "Is the iPhone 13 water-resistant?"
        },
        {
        "role": "assistant",
        "content": "Yes, the iPhone 13 is rated as water-resistant with an IP68 rating, which means it can withstand being submerged in water up to a certain depth."
        },
        {
        "role": "user",
        "content": "What is the storage capacity of the iPhone 13 Pro?"
        },
        {
        "role": "assistant",
        "content": "The iPhone 13 Pro is available in storage capacities of 128GB, 256GB, and 512GB."
        },
        {
        "role": "user",
        "content": "How can I update my iPhone's operating system?"
        },
        {
        "role": "assistant",
        "content": "You can update your iPhone's operating system by going to 'Settings' > 'General' > 'Software Update' and following the on-screen instructions."
        },
        {
        "role": "user",
        "content": "Does the iPhone 13 support 5G connectivity?"
        },
        {
        "role": "assistant",
        "content": "Yes, the iPhone 13 supports 5G connectivity for faster data speeds and improved network performance."
        },
        {
        "role": "user",
        "content": "Can I use wireless charging with the iPhone 13?"
        },
        {
        "role": "assistant",
        "content": "Yes, the iPhone 13 supports wireless charging using Qi-compatible chargers."
        },
        {
        "role": "user",
        "content": "What colors are available for the iPhone 13 Pro?"
        },
        {
        "role": "assistant",
        "content": "The iPhone 13 Pro is available in colors such as Graphite, Gold, Silver, and Sierra Blue"
        },
        {
        "role": "user",
        "content": "Does the iPhone 13 have a headphone jack?"
        },
        {
        "role": "assistant",
        "content": "No, the iPhone 13 does not have a headphone jack. It uses a Lightning port or wireless audio options."
        },
        {
        "role": "user",
        "content": "What is the warranty period for the iPhone 13?"
        },
        {
        "role": "assistant",
        "content": "Most existing iPhone accessories should be compatible with the iPhone 13, but it depends on the specific accessory."
        },
        {
        "role": "user",
        "content": "Can I use wireless charging with the iPhone 13?"
        },
        {
        "role": "assistant",
        "content": "Yes, the iPhone 13 supports wireless charging using Qi-compatible chargers."
        },
        {
        "role": "user",
        "content": "How can I contact Apple Support for assistance?"
        },
        {
        "role": "assistant",
        "content": "You can contact Apple Support through the Apple website, Apple Support app, or by calling the Apple Support phone number."
        },
        {
        "role": "user",
        "content": "\"Where can I purchase an iPhone 13?"
        },
        {
        "role": "assistant",
        "content": "You can purchase an iPhone 13 from authorized Apple retailers, Apple's official website, or through carrier stores"
        },
        {
        "role": "assistant",
        "content": "such as AT&T, Verizon, T-Mobile, or Sprint. Additionally, you can also buy the iPhone 13 from authorized third-party retailers like Best Buy, Walmart, or Target."
        },
        {
        "role": "assistant",
        "content": "You can purchase an iPhone 13 from authorized Apple retailers, Apple's official website, or through carrier stores."
        }
    ]
    new_user_prompt = {
    "role": "user",
    "content": new_user_prompt
    }
    conversation = messages + [new_user_prompt]
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response

    





def index(request):
    
    return render(request,"index.html")

  


                      


def endpoint(request):
    req = request.GET.get('query')
    converted_word = req.lower()
    
    result = query_chatgpt_api(converted_word)
    
    re = result['choices'][0]['message']['content']
    return JsonResponse({"result":re})
  
    
