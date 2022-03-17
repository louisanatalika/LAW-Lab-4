# [LAW] Lab 4: Implementasi CRUD
## Identitas
* Nama: Louisa Natalika Jovanna
* NPM : 1806205022

## Endpoint
1. **[READ]** GET    /books/ \
    Example: \
    ![GET ALL Books](https://user-images.githubusercontent.com/60333894/158632339-c0220007-cc85-4f04-8694-298c8d7032c4.PNG)


2. **[CREATE]** POST   /books/create/
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | title   | String   |
        | author   | String   |

    Example: \
    ![POST CREATE Book](https://user-images.githubusercontent.com/60333894/158632434-10b76bcf-b878-40e1-8344-d182a9c5df98.PNG)

3. **[READ]** GET    /books/{ID} \
    Example: \
    ![GET A Book](https://user-images.githubusercontent.com/60333894/158632548-4802a66a-fcdf-4db4-9d57-5e350450569e.PNG)

4. **[UPDATE]** PUT    /books/{ID}
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | title   | String (optional)  |
        | author   | String  (optional) |

    Example: \
    ![PUT UPDATE A Book](https://user-images.githubusercontent.com/60333894/158632643-955a9f4d-f8c0-4e67-bb58-aa26bc613f43.PNG)

5. **[DELETE]** DELETE /books/{ID} \
    Example: \
    ![DELETE A Book](https://user-images.githubusercontent.com/60333894/158632691-c702ebe5-d91d-46e1-acf6-895670767ff9.PNG)

6. **[CREATE]** POST   /books/post-image/ \
    Example: \
    ![POST Book Image](https://user-images.githubusercontent.com/60333894/158632750-45edbdab-5f81-4873-b901-50e344e9bd30.PNG)
    Uploaded file would be stored in /media/images: \
    ![POST Book Image Approved](https://user-images.githubusercontent.com/60333894/158632791-3ca1b871-2cc0-4fc5-8b1a-d05c7070fa42.PNG)


## Deployment
1. Deployed at: [Infralabs]()
