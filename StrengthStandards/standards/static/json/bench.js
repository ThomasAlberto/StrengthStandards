fetch('bench.json')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.getElementById('tableBody');
    data.data.forEach(rowData => {
      const row = document.createElement('tr');
      Object.values(rowData).forEach(cellData => {
        const cell = document.createElement('td');
        cell.textContent = cellData;
        row.appendChild(cell);
      });
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
