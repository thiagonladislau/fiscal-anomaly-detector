import pandas as pd

# Passo 1 - Carregamos os mesmos dados
df = pd.read_csv('fiscal_data.csv')

# Criamos uma coluna temporária para verificar a alíquota real da nota
# Regra: Imposto dividido pelo Valor da Nota
df['real_rate'] = df['calculated_icms'] / df['invoice_value']

# Definimos o que é suspeito: qualquer alíquota maior que 13% (margem de segurança)
threshold = 0.13

# Passo 2 - Filtramos o DataFrame para manter apenas as anomalias
anomalies = df[df['real_rate'] > threshold].copy()

# Organizamos por valor para focar no que dói mais no bolso (maiores erros primeiro)
anomalies = anomalies.sort_values(by='invoice_value', ascending=False)


# Passo 3 - Selecionamos apenas as colunas essenciais para o setor fiscal
final_report = anomalies[['invoice_id', 'vendor_name', 'vendor_cnpj', 'invoice_value', 'calculated_icms']]

# Salvamos em um novo arquivo para entregar à equipe
final_report.to_csv('audit_report_needed.csv', index=False)

print(f"📊 Relatório gerado! {len(final_report)} notas suspeitas encontradas.")
print("Arquivo 'audit_report_needed.csv' pronto para conferência.")