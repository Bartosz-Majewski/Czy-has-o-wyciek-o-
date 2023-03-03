### Czy twoje hasło jest bezpieczne?
Zapisz hasła, które chcesz przetestować w pliku tekstowym passwords.txt.
Program otwiera plik passwords.txt, a następnie przetwarza go linia po linii.
Jeśli hasło spełnia wszystkie wymogi dobrego hasła oraz jeżeli nie wyciekło ani razu
to powinno zostać zapisane do osobnego pliku o nazwie bezpieczne.txt.

#### Jak program sprawdza czy hasło wyciekło?
Program korzysta z zewnętrznego API "haveibeenpwnd". Hasła z Twojego pliku są haszowane korzystająć z algorytmu sha1.Następnie do serwisu 
haveibeenpwnd wysyłamy pierwszych pięć haszów hasła. Wysyłamy im tylko 5 pierwszych znaków hasha, ponieważ wysłanie całego hasza może spowodować,
że Twoje hasło wycieknie.
Serwis odpowie wszystkimi końcówkami hashy jakie zna "haveibeenpwnd" wraz z informacją ile razy dane hasło wyciekło.
Nastęnie porównujemy czy końcowka naszego hasza zgadza się, z którąś z usyskanych z API i uzysakujemy inforamcje czy sprawdzane hasło wyciekło.

#### Przyjęte wymogi bezpiecznego hasła:
● Musi mieć odpowiednią długość (minimum 8 znaków).<br>
● Musi zawierać przynajmniej jedną cyfrę.<br>
● Musi zawierać przynajmniej jeden znak specjalny.<br>
● Musi zawierać wielkie i małe litery.<br>

### Jak uruchomić program?
Pobierz repozytorium, w pliku tekstowym passwords.txt wpisz hasła(każde w nowej linii).
Uruchom plik validators.py
