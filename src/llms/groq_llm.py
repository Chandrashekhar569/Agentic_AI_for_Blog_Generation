from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class GroqLLM:
    """
    A wrapper class to initialize and return a Groq LLM instance using environment variables.

    Environment Variables:
        GROQ_API_KEY (str): The API key used to authenticate with Groq's LLM.

    Attributes:
        groq_api_key (str): Loaded API key from environment for Groq.
    """

    def __init__(self):
        """
        Load environment variables using dotenv.
        """
        load_dotenv()

    def get_llm(self):
        """
        Initialize and return a Groq language model instance.

        Returns:
            ChatGroq: A configured Groq chat model ready to be used.

        Raises:
            ValueError: If environment variables are missing or initialization fails.
        """
        try:
            # Load and assign Groq API key
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")

            # Instantiate Groq LLM with a specific model
            llm = ChatGroq(
                api_key=self.groq_api_key,
                model="meta-llama/llama-4-maverick-17b-128e-instruct"
            )

            # Uncomment below to switch to OpenAI (optional alternative)
            # os.environ["OPENAI_API_KEY"] = self.openai_api_key = os.getenv("OPENAI_API_KEY")
            # llm = ChatOpenAI(api_key=self.openai_api_key, model="gpt-4-turbo")
            
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")
