require "nokogiri"
require "open-uri"
require "json"
@doc=Nokogiri::HTML(open("https://flagpedia.net/index"))
@pays=[]
@doc.css("[data-area]").each do |x|
  begin
    pays={}
    pays["country"]=x.text.strip
    @doc2=Nokogiri::HTML(open("https://flagpedia.net"+x.attributes["href"].value+"/emoji"))
    hey=@doc2.css("table td")[1].text.gsub("&amp;","&")
    pays["unicode"]=hey
    p pays
    @pays<<pays
    File.write("public/temp.json", JSON.pretty_generate({"pays":@pays}))
  rescue
    next
  end
end

