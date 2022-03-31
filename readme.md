# [LAW] Lab 4: Implementasi CRUD
## Identitas
* Nama: Louisa Natalika Jovanna
* NPM : 1806205022

## Endpoint
1. **[READ]** GET    /books/ \
    Example: \
    ![GET ALL BOOKS](https://user-images.githubusercontent.com/60333894/160957735-f3667bab-a3c1-47be-98c9-6f6e6f212b6f.png)

2. **[CREATE]** POST   /books/create/city
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | name   | String   |
        | province   | String   |

    Example: \
    ![CREATE CITY](https://user-images.githubusercontent.com/60333894/160957900-33e0605b-1c51-4e22-bd97-b83533a33246.png)


3. **[READ]** GET    /books/{title} \
    Example: \
    ![GET A BOOK BY TITLE](https://user-images.githubusercontent.com/60333894/160957985-bb64a8ee-788c-4bbe-ab80-f28cf63a837f.png)


4. **[UPDATE]** PUT    /books/{ID}
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | title   | String (optional)  |
        | author   | String  (optional) |

    Example: \
    ![UPDATE A BOOK](https://user-images.githubusercontent.com/60333894/160958244-d36d926f-782f-46aa-8075-1048557098da.png)

5. **[DELETE]** DELETE /books/{ID} \
    Example: \
    ![DELETE A Book](https://user-images.githubusercontent.com/60333894/158632691-c702ebe5-d91d-46e1-acf6-895670767ff9.PNG)

6. **[CREATE]** POST   /books/post-image/ \
    Example: \
    ![POST Book Image](https://user-images.githubusercontent.com/60333894/158632750-45edbdab-5f81-4873-b901-50e344e9bd30.PNG)
    Uploaded file would be stored in /media/images: \
    ![POST Book Image Approved](https://user-images.githubusercontent.com/60333894/158632791-3ca1b871-2cc0-4fc5-8b1a-d05c7070fa42.PNG)


