<?php
function Conectarse()
{
   if (!($link=mysql_connect("localhost","root","s3rv3r")))
   {
      echo "Error conectando a la base de datos.";
      exit();
   }
   if (!mysql_select_db("asteriskcdrdb",$link))
   {
      echo "Error seleccionando la base de datos.";
      exit();
   }
   return $link;
}
?>
