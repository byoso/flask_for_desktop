


Do not forget to migrate from this directory:

```
#### Migrations
- Create the migration repository
```
$ flask db init
```
- make a new migration
```
$ flask db migrate -m "Initial"
```
- apply the migration
```
$ flask db upgrade
```
