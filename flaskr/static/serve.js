let preferences_data;

document.getElementById('generate-btn').addEventListener('click', async () => {
    const response = await fetch('/generate-preferences', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({number: document.getElementById('number').value})
    });
    const data = await response.json();
    preferences_data = data
    console.log(data);
    createBasicVisual(data)
});

// Calculer le mariage stable
document.getElementById('calculate-btn').addEventListener('click', async () => {
    const response = await fetch('/stable-marriage', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({preferences: preferences_data})
    });
    const data = await response.json();
    console.log(data);
    createResult(data)
});

function createBasicVisual(data) {
    const visual = document.querySelector('.visual');
    // Vider le contenu précédent
    visual.innerHTML = '';
    
    // Colonne gauche (Students)
    const leftColumn = document.createElement('div');
    leftColumn.className = 'column';
    leftColumn.innerHTML = '<h3>🧑‍🎓 Students</h3>';
    
    // Créer les éléments étudiants (s dans data)
    const numPeople = Object.keys(data.s).length;
    for (let index = 0; index < numPeople; index++) {
        const studentKey = Object.keys(data.s)[index];
        const preferences = data.s[studentKey];
        const student = document.createElement('div');
        student.className = 'basicItem';
        student.textContent = `Student ${index} : [${preferences.join(', ')}]`;
        leftColumn.appendChild(student);
    }


    // Colonne gauche (Students)
    const rightColumn = document.createElement('div');
    rightColumn.className = 'column';
    rightColumn.innerHTML = '<h3>🏫 Schools</h3>';
    
    for (let index = 0; index < numPeople; index++) {
        const studentKey = Object.keys(data.e)[index];
        const preferences = data.e[studentKey];
        const student = document.createElement('div');
        student.className = 'basicItem';
        student.textContent = `School ${index} : [${preferences.join(', ')}]`;
        rightColumn.appendChild(student);
    }
    
    visual.appendChild(leftColumn);
    visual.appendChild(rightColumn);
}
function createResult(data) {
    const rapport = document.querySelector('.rapport');
    // Vider le contenu précédent
    rapport.innerHTML = '';
    
    const result_data = data.metadata.result;
    const stats_data = data.metadata.satisfaction;
    
    // Section Results
    const resultSection = document.createElement('div');
    resultSection.className = 'result-section';
    resultSection.innerHTML = `
        <h3>📊 Results</h3>
        <div class="result-content">${result_data}</div>
    `;
    
    // Section Statistics
    const statsSection = document.createElement('div');
    statsSection.className = 'stats-section';
    statsSection.innerHTML = '<h3>📈 Satisfaction Statistics</h3>';
    
    // Moyennes globales
    const averagesDiv = document.createElement('div');
    averagesDiv.className = 'averages-container';
    averagesDiv.innerHTML = `
        <div class="stat-card global">
            <div class="stat-label">Global Satisfaction</div>
            <div class="stat-value">${stats_data["Average_global satisfaction"]}%</div>
        </div>
        <div class="stat-card student">
            <div class="stat-label">Student Satisfaction</div>
            <div class="stat-value">${stats_data["Average_student satisfaction"]}%</div>
        </div>
        <div class="stat-card school">
            <div class="stat-label">School Satisfaction</div>
            <div class="stat-value">${stats_data["Average_school satisfaction"]}%</div>
        </div>
    `;
    
    // Détails par entité
    const detailsDiv = document.createElement('div');
    detailsDiv.className = 'details-container';
    
    // Students satisfaction
    const studentsDetail = document.createElement('div');
    studentsDetail.className = 'detail-group';
    studentsDetail.innerHTML = '<h4>🧑‍🎓 Individual Students</h4>';
    stats_data.Students_satisfaction.forEach((sat, index) => {
        const item = document.createElement('div');
        item.className = 'detail-item';
        item.innerHTML = `
            <span>Student ${index}</span>
            <span class="satisfaction-bar">
                <span class="satisfaction-fill" style="width: ${sat}%"></span>
                <span class="satisfaction-text">${sat}%</span>
            </span>
        `;
        studentsDetail.appendChild(item);
    });
    
    // Schools satisfaction
    const schoolsDetail = document.createElement('div');
    schoolsDetail.className = 'detail-group';
    schoolsDetail.innerHTML = '<h4>🏫 Individual Schools</h4>';
    stats_data.Schools_satisfaction.forEach((sat, index) => {
        const item = document.createElement('div');
        item.className = 'detail-item';
        item.innerHTML = `
            <span>School ${index}</span>
            <span class="satisfaction-bar">
                <span class="satisfaction-fill" style="width: ${sat}%"></span>
                <span class="satisfaction-text">${sat}%</span>
            </span>
        `;
        schoolsDetail.appendChild(item);
    });
    
    detailsDiv.appendChild(studentsDetail);
    detailsDiv.appendChild(schoolsDetail);
    
    statsSection.appendChild(averagesDiv);
    statsSection.appendChild(detailsDiv);
    
    rapport.appendChild(resultSection);
    rapport.appendChild(statsSection);
}

function createVisual(data) {
    const visual = document.querySelector('.visual');
    visual.innerHTML = '';
    

    
    // Colonne gauche (Hommes)
    const leftColumn = document.createElement('div');
    leftColumn.className = 'column';
    leftColumn.innerHTML = '<h3>🧑‍🎓 Students</h3>';
    
    // Créer les éléments hommes (s dans data)
    const numPeople = Object.keys(data.s).length;
    for (let index = 0; index < numPeople; index++) {
        const studentKey = Object.keys(data.s)[index];
        const preferences = data.s[studentKey];
        
        const student = document.createElement('div');
        student.setAttribute('id', `s${index}`);
        student.className = 'item';
        
        // Créer le conteneur pour les préférences
        const preferencesContainer = create_Pref(preferences)
        
        // Créer le conteneur pour l'étudiant (icône + label)
        const studentInfo = document.createElement('div');
        studentInfo.className = 'student-info';

        // Créer l'icône
        const studentIcon = document.createElement('div');
        studentIcon.textContent = '🧑‍🎓';
        studentIcon.className = 'student-icon';

        // Créer le label
        const studentLabel = document.createElement('p');
        studentLabel.textContent = `Student ${index}`;
        studentLabel.className = 'student-label';

        // Ajouter l'icône et le label au conteneur
        studentInfo.appendChild(studentIcon);
        studentInfo.appendChild(studentLabel);

        // Ajouter les préférences puis les infos de l'étudiant
        student.appendChild(preferencesContainer);
        student.appendChild(studentInfo);
        
        leftColumn.appendChild(student);
    }
    
    visual.appendChild(leftColumn);
}

function create_Pref(preferences) {
    // Créer le conteneur pour les préférences
    const preferencesContainer = document.createElement('div');
    preferencesContainer.className = 'preferences';

    // Ajouter le crochet ouvrant
    const openBracket = document.createElement('span');
    openBracket.textContent = '[';
    openBracket.className = 'bracket';
    preferencesContainer.appendChild(openBracket);

    // Ajouter chaque préférence avec virgule
    preferences.forEach((pref, idx) => {
        const prefSpan = document.createElement('span');
        prefSpan.textContent = pref;
        prefSpan.className = 'pref-item';
        preferencesContainer.appendChild(prefSpan);
        
        // Ajouter la virgule sauf pour le dernier élément
        if (idx < preferences.length - 1) {
            const comma = document.createElement('span');
            comma.textContent = ', ';
            comma.className = 'separator';
            preferencesContainer.appendChild(comma);
        }
    });

    // Ajouter le crochet fermant
    const closeBracket = document.createElement('span');
    closeBracket.textContent = ']';
    closeBracket.className = 'bracket';
    preferencesContainer.appendChild(closeBracket);
    return preferencesContainer;
}