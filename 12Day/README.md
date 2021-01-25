### React simples

Subindo uma aplicação simples em REACT com node.js.

```
npx create-app-react <nome-aplicacao>
```

Tive problemas para subir o servidor por causa de um erro no webpack, para burlar o erro, crie o arquivo ```.env``` na raiz do projeto e coloque dentro:

```
SKIP_PREFLIGHT_CHECK=true
```

Para subir o projeto, só entre no diretorio e de um:

```
npm start
```

Ele vai subir o diretório SRC