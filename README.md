## Projeyi kendi lokalinizde çalıştırmak için aşağıdaki adımları izleyiniz.

#### Öncelikle pcnizde projeyi indireceğiniz bir klasör oluşturunuz. Klasör konumu dizini örneği: C:\users\eba\Desktop\calliope
#### VsCode'a girip terminali açınız. CMD, Powershell, Bash vb terminaller de tercih edilebilir.
#### cd komutu ile az önce yarattığınız dizine geliniz. ör: `cd \users\eba\Desktop\calliope`
#### `git clone https://github.com/eberkeaydin/calliope-api.git`  --> projeyi klonlayınız.
#### İndirmenin ardından yaratılan projeyi VsCode'da açınız.


#### Projeyi ayağa kaldırmak için Python environmenti kurmak gereklidir. venv kurulumu tavsiye edilir.
#### Pcnizde Python ve pip kurulumlarının bulunması gerekir. `python -v` ve `pip -V` komutları ile versiyon kontrolü yapabilirsiniz.
#### Pcnizde Python ve pip kurulumları var ise proje dizininde terminal üzerinden önce :
#### `py -m pip install --user virtualenv` ardından
#### `py -m venv env` komutları calıstırılarak sanal Python ortamları oluşturulur.
#### `.\env\Scripts\activate` komutu ile ortam aktifleştirilir. Terminal kapatılıp bir daha açılır.
#### Proje dizininde terminal üzerinden bu kez `pip install django` komutu ile Django indirilir 
#### `py manage.py runserver` komutu calıstırılır ve proje lokal hostta canlıya alınmıs olur.
#### lokal hostte /quiz URL'ine girip son gelişmeleri; /admin URL girip database gelismelerini kontrol edebilirsiniz.


