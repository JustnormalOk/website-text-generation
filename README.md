<img width="621" alt="Screenshot 2024-12-22 at 22 28 44" src="https://github.com/user-attachments/assets/0b05a14a-5b18-42af-a4a4-f0ed4a831e86" />

# website-text-generation
An AI web chat that has multiple characters, customizeable, free and even open-source! 

# How it works:
It works when you chat, create character, and even roleplay!

<img width="1192" alt="Screenshot 2024-12-22 at 22 29 08" src="https://github.com/user-attachments/assets/e7d5336a-266c-42d1-8ac7-7a180ce1920c" />

// Image 1: The main screen included a characted called Adam //

Chatting

<img width="427" alt="Screenshot 2024-12-22 at 22 43 10" src="https://github.com/user-attachments/assets/01cdcea8-77ef-4aed-86da-92a41ae7ee5f" />
// Image 2: A chat with Adam //

you chat, like that.

One last feature, it also works in offline, during power outage if you're bored! It only operates the AI on your laptop!

# Instructions:
**Notice**: This ai website may not work with some commands
If its said: Error: Cannot read properties of null (reading 'src')
Refresh the page so you could see again
**Second Notice**: The pfp may not visible in the chat, so you could help me fix the code, or wait I'll update it.

## Installitation Process:
1. **Install this repo**: It's easy, just install, unzip and open VS code, put it in VS code with this project file, and done!
2. **Install LM Studio**: It's easy either, [click here](https://lmstudio.ai/) to go on LM studio
3. **Install Models**: Install the models, by these conditions:

For Computers:
| **Model Size** | **Parameters (Billion)** | **VRAM Required (GB)** | **System RAM (GB)** | **Storage (GB)** | **Use Case**                           | **Notes**                                             |
|----------------|--------------------------|-------------------------|---------------------|------------------|-----------------------------------------|------------------------------------------------------|
| **3B**         | 3 Billion               | 6-8 GB                 | 12-16 GB           | ~2 GB            | Small-scale tasks (chatbots, assistants) | Lightweight, works on mid-tier GPUs like RTX 3060.   |
| **7B**         | 7 Billion               | 10-12 GB               | 16-32 GB           | ~4 GB            | Intermediate tasks (text generation, Q&A) | Popular for local models like LLaMA-7B.              |
| **13B**        | 13 Billion              | 16-20 GB               | 32 GB+             | ~8 GB            | Advanced tasks (summarization, complex NLP) | Needs high-end GPUs like RTX 3090 or 4090.           |
| **30B**        | 30 Billion              | 24-32 GB               | 64 GB+             | ~15 GB           | High-complexity NLP tasks               | Multiple GPUs required for inference.               |
| **65B**        | 65 Billion              | 40-48 GB               | 128 GB+            | ~35 GB           | Large-scale research models             | Works only with A100/H100 or multiple GPUs in parallel. |
| **175B**       | 175 Billion             | 80 GB+                 | 256 GB+            | ~90 GB           | GPT-like models for enterprise apps     | Needs clusters or cloud computing like AWS/GCP.      |

For laptops and macbooks:
| **Model Size** | **Parameters (Billion)** | **VRAM Required (GB)** | **System RAM (GB)** | **Storage (GB)** | **Laptop Requirements**                      | **MacBook Requirements**                                 | **Notes**                                             |
|----------------|--------------------------|-------------------------|---------------------|------------------|------------------------------------------------|---------------------------------------------------------|------------------------------------------------------|
| **3B**         | 3 Billion               | 6-8 GB                 | 12-16 GB           | ~2 GB            | Any gaming laptop with RTX 3060 or better    | Any MacBook with M1/M2 (8 GB RAM)                       | Lightweight, works for small-scale tasks.           |
| **7B**         | 7 Billion               | 10-12 GB               | 16-32 GB           | ~4 GB            | RTX 3070 laptop with 16 GB RAM or better     | MacBook Pro M1/M2 with 16 GB RAM                        | Great for chatbots and Q&A, even on MacBooks.        |
| **13B**        | 13 Billion              | 16-20 GB               | 32 GB+             | ~8 GB            | RTX 3080/4080 laptop, 32 GB RAM recommended  | MacBook Pro M1/M2 with 32 GB RAM (Apple Silicon only)   | Advanced NLP tasks; needs more RAM for performance. |
| **30B**        | 30 Billion              | 24-32 GB               | 64 GB+             | ~15 GB           | Dual GPUs (e.g., RTX 4090 SLI) or workstation| Mac Studio with M1 Ultra, 64 GB RAM                     | Handles high-complexity AI tasks; GPU-intensive.     |
| **65B**        | 65 Billion              | 40-48 GB               | 128 GB+            | ~35 GB           | High-end workstations with A100 GPUs         | Unsupported on MacBooks; requires Mac Studio or clusters| Research models; not for casual laptops.             |
| **175B**       | 175 Billion             | 80 GB+                 | 256 GB+            | ~90 GB           | Multi-node clusters or AWS/GCP               | Not feasible locally; requires cloud computing          | Enterprise-level models like GPT-3.                 |

> **Note**: Llama Studio requires Apple Silicon (M1/M2). For larger models, cloud computing or workstations with multiple GPUs are recommended.

5. **Install Python Packages**: Install by this command in terminal or command prompt: `pip3 install flask requests`

## Run the AI and the server:
1. Go on LM studio, press Developer under the tab of the app

<img width="390" alt="Screenshot 2024-12-22 at 22 53 23" src="https://github.com/user-attachments/assets/a13bb7bb-2843-4b96-b3f9-4d398290b86d" />
// Image 3: Showing Developer button //

2. Press the "Select a model to load"

   <img width="687" alt="Screenshot 2024-12-22 at 22 54 07" src="https://github.com/user-attachments/assets/e2d4ee9c-59b3-4010-b280-24df02442233" />

// Image 4: Showing the Select model part //

- After that, press the AI model you installed

3. Customize these settings:

<img width="691" alt="Screenshot 2024-12-22 at 22 55 30" src="https://github.com/user-attachments/assets/7780b9e3-4bca-4f58-9572-1b89f9df4f05" />

// Image 5: Settings //

- If your computer/laptop is weak, reduce the GPU offload

- Additional Note: turn on Keep Model in Memory

4. After that, press Load Model
5. After loading model, go in VS code, press app.py
7. Create a file named `uploads` in static folders
8. Go to the tab Run and Debug, and press Run and Debug
9. If it's running, go into the provided link
10. Done!! That's how you do it.

**YOUTUBE VIDEO TUTORIAL**: https://www.youtube.com/watch?v=B-3XbZKdfCQ

# Notices:
1. Don't forget to set the name and the profile picture, or else it will not send the message
2. There may bugs so I'll think about updates
3. The UI design may not look good but I'll think that plan to update it
4. The response time from your computer may be depending on the processor including the GPU, CPU, RAM and Memory
5. If you can't go in the website with the other devices, the device may not on the same as the **Server Network**

