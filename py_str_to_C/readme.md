# Implémentation du type <'str'> python en C++

Les méthodes de classe fonctionnes comme celle de python, pour les méthodes dont le retour est un tableaux/liste, j'ai choisis d'implementé ça avec des vecteurs ( cf #include \<vector> )

Plus ou moins toutes les méthodes ne changent pas la valeurs de l'attribut.

### Redefinition des opérateurs :

* opérateur **=**

```c++
pythString a ("YOLO");
pythString b ("HELLO");
a = b;
std::cout<<a.getAttr();
// HELLO
```

* opérateur **+=**

```c++
pythString a ("YOLO");
pythString b ("HELLO");
a += b;
std::cout<<a.getAttr();
// YOLOHELLO
```

* opérateur **<<**

```c++
pythString a ("YOLO");
std::cout<<a;
// YOLO
```

* opérateur **[]**

  Retourne un 'CHAR' et non un 'STRING'

```c++
pythString a("YOLO");
std::cout<<a[0];
// Y
```

