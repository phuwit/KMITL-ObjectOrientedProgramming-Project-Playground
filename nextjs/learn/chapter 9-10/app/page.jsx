import LikeButton from "./like-button";


function Header({title}) {
    return(<h1>My name is {title ? title : 'undefined'}</h1>);
}

export default function HomePage() {
    const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];

    return <div>
        <Header title='react' />
        <Header title='not svelte' />

        <ul>
            {
                names.map(name => (
                    <li key={name}>{name}</li>
                ))
            }
        </ul>

        <LikeButton />
    </div>
}