# [LAW] Lab 4: Implementasi CRUD
## Identitas
* Nama: Louisa Natalika Jovanna
* NPM : 1806205022

## Endpoint
1. **[READ]** GET    /books/ \
    Example: \
    ![Get all boooks]()

2. **[CREATE]** POST   /books/create/
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | title   | String   |
        | author   | String   |

    Example: \
    ![Create a book]()

3. **[READ]** GET    /books/{ID} \
    Example: \
    ![Get a book]()

4. **[UPDATE]** PUT    /books/{ID}
    * Content-type:
        * form-data
    * Request Body:
        | Key       | Type  |
        | :---:     | :-:   |
        | title   | String (optional)  |
        | author   | String  (optional) |

    Example: \
    ![Update a book]()

5. **[DELETE]** DELETE /books/{ID} \
    Example: \
    ![Delete a book]()

6. **[CREATE]** POST   /books/post-image/ \
    Example: \
    ![Upload an image]()
    Uploaded file: \
    ![Uploaded image]()


## Deployment
1. Deployed at: [Infralabs](https://simplecarapi.herokuapp.com/)
