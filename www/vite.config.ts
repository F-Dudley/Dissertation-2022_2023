import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react-swc';
import tsconfigPaths from 'vite-tsconfig-paths';
import Pages from 'vite-plugin-pages';

// https://vitejs.dev/config/
export default ({ mode }: {mode: string}) => {

	const env = loadEnv(mode, process.cwd(), 'SERVER_');

	const isProduction = mode === 'production';

	const basePath = isProduction ? env.SERVER_BASE_PATH : '/';

	console.log('Using Base Path: ', basePath)
	console.log('Using Mode: ', mode)

	return defineConfig({
		base: '/',
		server: {
			port: 3000,
		},
		plugins: [
			react(),
			tsconfigPaths(),
			Pages({
				extensions: ['tsx', 'jsx'],
			}),
		],
	});
};