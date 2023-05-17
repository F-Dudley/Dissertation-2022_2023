import Root from '@/components/tunnels/Root';
import { useNavigate } from 'react-router';

const PageNotFound = () => {
	const navigator = useNavigate();

	return (
		<Root.In>
			<main className="absolute z-10 w-full h-full m-auto flex flex-col items-center justify-center text-accent">
				<div className="bg-tertiary rounded-md border-2 border-accent">
					<div className="p-5 flex items-center justify-center">
						<h1>Page not found.</h1>
					</div>
					<div className="p-5">
						<button
							className="bg-secondary rounded-md hover:bg-primary"
							onClick={() => navigator('/')}
						>
							Return to Home
						</button>
					</div>
				</div>
			</main>
		</Root.In>
	);
};

export default PageNotFound;
