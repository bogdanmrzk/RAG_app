# RAG_app

RAG chat API about Django Framework

## What is rag app  created for

This is DRF API chat, built to answer simple questions
about Django Framework

> [!IMPORTANT]
> You must have running instance of ollama3.2
>
> Ollama installation/running
>
> ` curl -fsSL https://ollama.com/install.sh | sh `
>
> ` ollama serve `
>
> ` ollama pull llama3.2 `

## Question samples

--------------------------------------------------------------------------------------------------------------------------

> request
`POST /apiv1/chat/ask`

`curl -X POST -H 'Content-Type: application/json' -d '{"question":"what is django forms?"}' -N localhost:8000/apiv1/chat/ask/`

> response
```
Django Forms is a built-in library in Django that provides a simple way to handle form data and validation. It allows you to define forms as classes or functions, which can be used to validate user input from forms.

The main features of Django Forms include:

* Automatic validation of form fields
* Ability to tie forms to models, enabling seamless CRUD operations on database entries

This makes it easier for developers to create secure and robust forms in their Django applications.

Forms are particularly useful when you want to enforce certain rules or constraints on user input, such as email addresses, phone numbers, or dates. By using Django Forms, you can ensure that your application is more secure and user-friendly.
```

--------------------------------------------------------------------------------------------------------------------------

> request
`POST /apiv1/chat/ask`

`curl -X POST -H 'Content-Type: application/json' -d '{"question":"what is django signals"}' -N localhost:8000/apiv1/chat/ask/`

> response
```
Based on the data provided, it seems that Django Signals are a way for different parts of an application to communicate with each other.

According to the table, "allow" indicates that signals can be sent and received by applications. 

In more detail, when certain actions occur elsewhere in the system (e.g., when a user is created or updated), Django can send a signal to other parts of the application that are listening for these events. This allows different components to react to these changes without having to know about each other's internal workings.

I don't have more information on this topic, but it appears to be related to decoupling and event-driven architecture in Django applications.  
```

