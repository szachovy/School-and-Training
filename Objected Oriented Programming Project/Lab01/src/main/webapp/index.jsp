<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Lab01 Formularz</title>
</head>
<body>
  <form method="post" action="calculate">
        Wnioskowana rata kredytu: <br />
        <input type="text" name="kredyt" /><br /> <br />
        Ilość rat: <br />
        <input type="text" name="raty" /><br /> <br />
        Oprocentowanie (w procentach w skali roku): <br />
        <input type="text" name="oprocentowanie" /><br /><br /> 
        Opłata stała: <br />
        <input type="text" name="oplata" /><br /> <br />
        Rodzaj rat: <br />
        Rata malejąca
        <input type="radio" name="rodzaj" value="maleje" checked/><br /> 
        Rata stała 
        <input type="radio" name="rodzaj" value="stala"/><br /> <br />
        <input type="submit" value="zatwierdz">
    </form>   
</body>
</html>