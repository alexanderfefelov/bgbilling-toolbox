# bgdl-reader

## Требования

Для сборки необходимы:

* git <https://git-scm.com/downloads>
* sbt <http://www.scala-sbt.org/>
* JDK 8

Для выполнения необходимы:

* JRE 8

## Сборка из исходных кодов

Для сборки выполните команды

    git https://github.com/alexanderfefelov/bgbilling-toolbox.git
    cd bgbilling-toolbox/bgdl-reader
    sbt assembly

В случае успеха в каталоге `target\scala-2.12` будет создан файл `bbr.jar`.

## Запуск

Для запуска выполните команду

    java -jar bbr.jar [параметры]

Для получения списка всех параметров выполните команду

    java -jar bbr.jar --help
