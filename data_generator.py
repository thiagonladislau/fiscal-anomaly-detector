import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup - 1000 fiscal records
np.random.seed(42)
n_records = 1000

# 2. Generating Realistic Mock Data
# Simulating 10 different suppliers
suppliers_cnpj = [f"{i:02d}.123.456/0001-{i:02d}" for i in range(1, 11)]
suppliers_names = [f"Supplier Enterprise {i:02d} Ltd" for i in range(1, 11)]

data = {
    'invoice_id': range(1, n_records + 1),
    'issue_date': [datetime(2026, 4, 1) + timedelta(days=np.random.randint(0, 30)) for _ in range(n_records)],
    'vendor_cnpj': np.random.choice(suppliers_cnpj, n_records),
    'vendor_name': "", # Will be mapped below
    'invoice_value': np.random.uniform(500, 15000, n_records),
    'cfop': np.random.choice([5102, 5405, 6102], n_records),
    'icms_rate': 0.12
}

df = pd.DataFrame(data)

# Mapping names to CNPJs
cnpj_to_name = dict(zip(suppliers_cnpj, suppliers_names))
df['vendor_name'] = df['vendor_cnpj'].map(cnpj_to_name)

# 3. Calculating the correct ICMS tax
df['calculated_icms'] = df['invoice_value'] * df['icms_rate']

# 4. Creating "Anomalies" (The "Queixo Caído" part)
# We corrupt 5% of the taxes to simulate errors
anomalous_indices = np.random.choice(df.index, size=50, replace=False)
df.loc[anomalous_indices, 'calculated_icms'] = df['calculated_icms'] * 1.5

# 5. Save to CSV
df.to_csv('tax_data.csv', index=False)

print("✅ Success! 'tax_data.csv' updated with CNPJ, Vendor Names, and Dates.")

# --- RESUMO (PORTUGUÊS) ---
# Adicionamos colunas reais: CNPJ, Razão Social e Data de Emissão.
# O script agora simula 10 fornecedores diferentes distribuídos em 1000 notas.
# Isso permite que a IA aprenda se um fornecedor específico erra mais que os outros.