from codeinterpreterapi import CodeInterpreterSession, File

from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FILE_PATH = os.getenv("FILE_PATH")


async def main():
    files = [
        File.from_path(FILE_PATH),
    ]

    # context manager for auto start/stop of the session
    async with CodeInterpreterSession(openai_api_key=OPENAI_API_KEY) as session:

        while True:
            # define the user request
            user_request = input("Please enter your instruction, or type 'exit' to quit: ")

            # Exit condition
            if user_request.lower() == "exit":
                break

            # generate the response
            response = await session.generate_response(
                user_request, files=files
            )

            # output to the user
            print("AI: ", response.content)
            for file in response.files:
                file.show_image()


if __name__ == "__main__":
    import asyncio
    # run the async function
    asyncio.run(main())
