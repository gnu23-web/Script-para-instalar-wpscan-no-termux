import os

def instalar_wpscan():
    print("\n[+] Atualizando pacotes...")
    os.system("pkg update -y && pkg upgrade -y")
    
    print("\n[+] Instalando dependências necessárias...")
    os.system("pkg install ruby libxml2 libxslt zlib clang make build-essential git -y")
    
    print("\n[+] Instalando nokogiri com bibliotecas do sistema...")
    os.system("gem install nokogiri -- --use-system-libraries")
    
    print("\n[+] Configurando bundler para usar bibliotecas do sistema...")
    os.system("bundle config build.nokogiri --use-system-libraries")
    
    print("\n[+] Atualizando RubyGems e Bundler...")
    os.system("gem update --system")
    os.system("gem install bundler")
    
    print("\n[+] Instalando WPScan...")
    os.system("gem install wpscan")
    
    print("\n[+] Corrigindo possível erro no arquivo 'libc.rb' da gem Ethon...")
    
    # Localizar o arquivo libc.rb
    print("[+] Localizando o arquivo 'libc.rb'...")
    path = os.popen("find /data/data/com.termux/files/usr/lib/ruby/gems/3.4.0/gems/ethon-* -name 'libc.rb'").read().strip()
    
    if path:
        print(f"[+] Arquivo encontrado em: {path}")
        print("[+] Aplicando correção no arquivo 'libc.rb'...")
        
        # Código corrigido para substituir no arquivo libc.rb
        codigo_corrigido = """# frozen_string_literal: true
module Ethon

  # FFI Wrapper module for Libc.
  #
  # @api private
  module Libc
    extend FFI::Library
    ffi_lib 'c'

    # :nodoc:
    def self.windows?
      Gem.win_platform?
    end

    unless windows?
      # Substituímos a função getdtablesize por um valor fixo, já que ela não está disponível no Android.
      def self.getdtablesize
        1024 # Retorna um valor fixo como fallback.
      end

      attach_function :free, [:pointer], :void
    end
  end
end
"""
        # Substituir o conteúdo do arquivo libc.rb
        with open(path, "w") as file:
            file.write(codigo_corrigido)
        
        print("[+] Correção aplicada com sucesso!")
    else:
        print("[-] Arquivo 'libc.rb' não encontrado. Verifique se a gem Ethon está instalada corretamente.")
    
    print("\n[+] WPScan instalado e configurado! Para usar, execute:")
    print("wpscan --help")

if __name__ == "__main__":
    print("=== Script Automático de Instalação do WPScan no Termux By: Termux Brasil 2025 ===")
    instalar_wpscan()
