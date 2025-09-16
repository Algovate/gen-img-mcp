import os
import gradio as gr
from dashscope import ImageSynthesis
from dotenv import load_dotenv
from http import HTTPStatus
import requests
from PIL import Image
import io

# Load environment variables
load_dotenv()

def generate_image(prompt: str, model_name: str) -> any:
    """
    Generate an image from text prompt using DashScope ImageSynthesis

    Args:
        prompt: Text description for image generation
        model_name: Selected model for image generation

    Returns:
        Generated PIL image or None if failed
    """
    try:
        # Use API key from environment variable
        api_key = os.environ.get("DASHSCOPE_API_KEY")

        if not api_key:
            raise ValueError("No DASHSCOPE_API_KEY found in environment variables")

        # Generate image using DashScope
        rsp = ImageSynthesis.call(
            api_key=api_key,
            model=model_name,
            prompt=prompt,
            n=1,
            size='1024*1024'
        )

        if rsp.status_code == HTTPStatus.OK:
            # Download the generated image
            result = rsp.output.results[0]
            response = requests.get(result.url, timeout=30)

            # Convert to PIL Image
            image = Image.open(io.BytesIO(response.content))
            return image
        else:
            print(f"ImageSynthesis failed: {rsp.code} - {rsp.message}")
            return None

    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Available models for text-to-image with DashScope
models = [
    # "wan2.1-t2i-turbo",
    "wan2.2-t2i-flash",
]

# Create the Gradio interface using Gradio 4 interface
def create_interface():
    with gr.Blocks(title="Text-to-Image Generator", theme=gr.themes.Soft()) as interface:
        gr.Markdown("# 🎨 Text-to-Image Generator")
        gr.Markdown("Generate stunning images from text descriptions using DashScope wan models!")

        with gr.Row():
            with gr.Column():
                prompt_input = gr.Textbox(
                    label="📝 Enter your prompt",
                    placeholder="Enter your image description here...",
                    lines=3
                )

                model_dropdown = gr.Dropdown(
                    choices=models,
                    value=models[0],
                    label="🤖 Select Model"
                )

                generate_btn = gr.Button("✨ Generate Image", variant="primary")

            with gr.Column():
                output_image = gr.Image(label="🖼️ Generated Image", type="pil")

        # Event handlers
        generate_btn.click(
            fn=generate_image,
            inputs=[prompt_input, model_dropdown],
            outputs=output_image
        )

        gr.Markdown("---")
        gr.Markdown("**Note:** Make sure to set your DashScope API key in the `.env` file as `DASHSCOPE_API_KEY=your_api_key_here`. You can get an API key at [Alibaba Cloud DashScope Console](https://dashscope.console.aliyun.com/)")

    return interface

if __name__ == "__main__":
    # Check if DASHSCOPE_API_KEY is available
    if not os.environ.get("DASHSCOPE_API_KEY"):
        print("⚠️  Warning: DASHSCOPE_API_KEY not found in environment variables.")
        print("Please set your DashScope API key in the .env file as DASHSCOPE_API_KEY=your_api_key_here")

    # Create and launch the app
    demo = create_interface()
    # Launch without API documentation to avoid schema issues
    demo.launch(share=False, show_api=False)