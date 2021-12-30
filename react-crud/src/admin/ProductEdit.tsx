import React, {PropsWithRef, SyntheticEvent, useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Redirect} from "react-router-dom";
import {Product} from "../interfaces/product";

const ProductEdit = (props: PropsWithRef<any>) => {
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false)

    useEffect(() => {
        const getProduct = async() =>{
            const response = await fetch(`http://localhost:8000/api/products/${props.match.params.id}`);
            const data : Product = await response.json();

            setTitle(data.title);
            setImage(data.image);
        };

        getProduct();
    }, []);

    const submit = async (event: SyntheticEvent) => {
        event.preventDefault()

        await fetch(`http://localhost:8000/api/products/${props.match.params.id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(
                    {
                        title,
                        image
                    }
                )
            });
        setRedirect(true)
    }

    if(redirect){
        return <Redirect to={'/admin/products'}/>
    }

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"
                           defaultValue={title}
                           onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"
                           defaultValue={image}
                           onChange={e => setImage(e.target.value)}
                    />
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>

        </Wrapper>
    );
};

export default ProductEdit;