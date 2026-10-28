# Bash — Registro de aprendizaje

## 1. ¿Qué es Bash?

Bash es un intérprete de comandos o shell. Permite ejecutar comandos, iniciar programas y automatizar tareas mediante scripts.

Bash no es lo mismo que Linux: Linux es un sistema operativo y Bash es una herramienta que puede utilizarse en Linux y otros entornos.

## 2. Comandos aprendidos

### `ls`

**Propósito:** mostrar los archivos y directorios de una ubicación.

**Sintaxis:**

```bash
ls
```

**Ejemplo:** ejecutar `ls` desde la raíz del repositorio para observar su estructura.

### `cat`

**Propósito:** mostrar el contenido de un archivo de texto.

**Sintaxis:**

```bash
cat ruta/del/archivo
```

**Ejemplo:**

```bash
cat README.md
```

Este comando lee el archivo, pero no lo modifica.

### `mkdir`

**Propósito:** crear directorios.

**Sintaxis:**

```bash
mkdir nombre_directorio
```

**Opción aprendida:**

```bash
mkdir -p silex_lab/documentation
```

La opción `-p` permite crear los directorios intermedios que falten y evita errores si ya existen.

### `touch`

**Propósito:** crear un archivo vacío si no existe.

**Ejemplo:**

```bash
touch silex_lab/documentation/bash.md
```

Si el archivo ya existe, `touch` actualiza sus marcas de tiempo; no borra su contenido.

### `mv`

**Propósito:** mover archivos o cambiarles el nombre.

**Ejemplo:**

```bash
mv nombre_anterior nombre_nuevo
```

También puede utilizarse para cambiar el nombre de un directorio, siempre que la operación sea válida.

## 3. Conceptos importantes

- **Terminal:** interfaz desde la que escribimos comandos.
- **Shell:** programa que interpreta y ejecuta esos comandos.
- **Directorio:** ubicación que contiene archivos y otros directorios.
- **Ruta:** dirección que identifica dónde se encuentra un archivo o directorio.
- **Ruta relativa:** se interpreta desde el directorio actual.
- **Repositorio:** espacio de trabajo cuyo historial de cambios administra Git.

## 4. Cómo aprendemos con SÍLEX

Para cada comando nuevo registraremos:

1. Nombre y propósito.
2. Sintaxis y significado de sus partes.
3. Ejemplo práctico.
4. Resultado observado.
5. Errores encontrados y soluciones.
6. Aplicación en el proyecto.

## 5. Estado

Este documento recoge los comandos que ya hemos encontrado durante el trabajo. Los ejemplos se ampliarán a medida que los practiquemos y verifiquemos.

### 6. Comandos basicos de terminal:

- `Cat` : sirve para mostrar el contenido de un archivo
- `Ls` : sirve para listar los archivos y diretorios de una ubicacion  
- `Pwd` : sirve para mostrar la ruta del directorio del trabajo actual