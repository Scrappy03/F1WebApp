document.addEventListener('DOMContentLoaded', function () {
    const teamColors = {
        'Williams Racing': '#64C4FF',
        'Oracle Red Bull Racing': '#3671C6',
        'Visa Cash App Racing Bulls Formula One Team': '#6692FF',
        'McLaren Formula 1 Team': '#FF8000',
        'Stake F1 Team Kick Sauber': '#52E252',
        'MoneyGram Haas F1 Team': '#B6BABD',
        'Scuderia Ferrari HP': '#E80020',
        'Aston Martin Aramco Formula One Team': '#229971',
        'Alpine': '#0093CC',
        'Mercedes-AMG': '#27F4D2'
    };

    // Debug: Log all available team names
    console.log('Available teams:', Object.keys(teamColors));

    document.querySelectorAll('[data-team]').forEach(element => {
        const rawTeamName = element.dataset.team;
        console.log('Raw team name from data-team:', rawTeamName);

        // Try to find the exact match first
        if (teamColors[rawTeamName]) {
            console.log('Found exact match for:', rawTeamName);
            applyTeamStyles(element, teamColors[rawTeamName], rawTeamName);
        } else {
            console.warn('No exact match found for:', rawTeamName);
            // Try to find a case-insensitive match
            const matchingTeam = Object.keys(teamColors).find(team =>
                team.toLowerCase() === rawTeamName.toLowerCase()
            );
            if (matchingTeam) {
                console.log('Found case-insensitive match:', matchingTeam);
                applyTeamStyles(element, teamColors[matchingTeam], matchingTeam);
            } else {
                console.error('No match found for team:', rawTeamName);
            }
        }
    });

    function applyTeamStyles(element, teamColor, teamName) {
        console.log('Applying styles for:', teamName, 'with color:', teamColor);

        if (element.classList.contains('team-title')) {
            element.style.borderBottomColor = teamColor;
            element.style.color = teamColor;
        } else if (element.classList.contains('card')) {
            applyCardStyles(element, teamColor);
        }
    }

    function applyCardStyles(card, teamColor) {
        // Card background and border
        card.style.background = `linear-gradient(145deg, var(--dark-gray), rgba(${hexToRgb(teamColor)}, 0.15))`;
        card.style.borderColor = teamColor;

        // Style the corner triangle with team color
        card.style.setProperty('--corner-color', teamColor);

        // Driver number with team color
        const driverNumber = card.querySelector('.driver-number');
        if (driverNumber) {
            driverNumber.style.background = teamColor;
            driverNumber.style.color = isLightColor(teamColor) ? '#000000' : '#FFFFFF';
        }

        // Card title border
        const cardTitle = card.querySelector('.card-title');
        if (cardTitle) {
            cardTitle.style.borderLeftColor = teamColor;
        }

        // Add hover effects
        applyHoverEffects(card, teamColor);
    }

    function applyHoverEffects(card, teamColor) {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-3px)';
            card.style.boxShadow = `0 5px 20px rgba(0, 0, 0, 0.3), 0 0 15px rgba(${hexToRgb(teamColor)}, 0.3)`;
            card.style.borderColor = `rgba(${hexToRgb(teamColor)}, 0.5)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'none';
            card.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.2)';
            card.style.borderColor = teamColor;
        });

        // Stat items hover effect
        card.querySelectorAll('.stat-item').forEach(item => {
            item.addEventListener('mouseenter', () => {
                item.style.transform = 'translateY(-2px)';
                item.style.background = `rgba(${hexToRgb(teamColor)}, 0.1)`;
            });

            item.addEventListener('mouseleave', () => {
                item.style.transform = 'none';
                item.style.background = 'rgba(255, 255, 255, 0.03)';
            });
        });
    }
});

// Helper function to convert hex to RGB
function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ?
        `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}`
        : null;
}

// Helper function for transitions
function applyTransition(element, properties = ['all']) {
    element.style.transition = properties.map(prop => `${prop} 0.3s ease`).join(', ');
}

// Helper function to check if a color is light
function isLightColor(color) {
    const rgb = hexToRgb(color).split(',').map(Number);
    const brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000;
    return brightness > 155;
}
