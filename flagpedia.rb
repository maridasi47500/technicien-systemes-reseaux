require "nokogiri"
require "open-uri"
require "json"
@doc=Nokogiri::HTML(open("https://flagpedia.net/index"))
@pays=[]
@doc.css("[data-area]").each do |x|
  pays={}
  pays["country"]=x.text
  @doc2=Nokogiri::HTML(URI.open(x.attributes["href"].value+"/emoji"))
  hey=@doc2.css("table td")[1].text.gsub("&amp;","&")
  pays["unicode"]=hey
  @pays<<pays

end
File.write("public/temp.json", JSON.pretty_generate({"pays":@pays}))
