from openai import OpenAI

client = OpenAI()

with open("test\\prompt_example.txt", "r", encoding="utf-8") as f:
    prompt = f.read()


class ConnectOpenAI:
    def __init__(self):
        self.assistant = client.beta.assistants.create(
          name="Example_AItuber",
          instructions=prompt,
          model="gpt-4o-mini",
        )
        pass

    def create_thread(self):
        self.thread = client.beta.threads.create()
        return self.thread

    def create_chat(self, thread, question):
        print("Waiting for API response... ")
        print(self.thread.id)
        if not question:
            question = question
        messages = client.beta.threads.messages.create(
          thread_id=self.thread.id,
          role="user",
          content=question
        )

        run = client.beta.threads.runs.create_and_poll(
          model="gpt-4o-mini",
          thread_id=self.thread.id,
          assistant_id=self.assistant.id,
        )
        if run.status == 'completed':
            messages = list(client.beta.threads.messages.list(
                thread_id=self.thread.id
                )
            )
            print(f"prompt tokens: {run.usage.prompt_tokens}")
            print(f"completion tokens: {run.usage.completion_tokens}")
            print(f"{messages[0].content[0].text.value}")
            question = None
            return messages[0].content[0].text.value

        else:
            print(run.status)
            print(run.incomplete_details)
            client.beta.threads.delete(self.thread.id)
            thread = self.create_thread()
            self.create_chat(thread, question)


if __name__ == '__main__':
    print(prompt)
    adapter = ConnectOpenAI()
    thread = adapter.create_thread()
    response_text = adapter.create_chat(thread, "please introduce yourself")
