/** @type {import('tailwindcss').Config} */

export default {
	content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
	theme: {
		extend: {
			colors: {
				primary: '#5D6464',
				secondary: '#374148',
				tertiary: '#282930',

				accent: '#B4AE96',
				highlight: '#E7DEC1',
			},
		},
		plugins: [],
	},
};
