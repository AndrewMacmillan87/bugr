import React from "react";

import PropTypes from "prop-types";

import "./delete.css";

export const Delete = ({ extraClasses, revealFunc, onClick, type }) => {
    const deleteClasses = extraClasses
        ? `delete-project-container ${extraClasses}`
        : "delete-project-container";

    return (
        <div className={deleteClasses}>
            <p className='delete-project-msg'>Delete {type}?</p>
            <div className='delete-project-btn-container'>
                <button className='delete-project-btn'>
                    <i
                        className='do-delete fas fa-check-circle'
                        onClick={() => {
                            onClick();
                            revealFunc("");
                        }}></i>
                </button>
                <button className='delete-project-btn'>
                    <i
                        className='do-not-delete fas fa-times-circle'
                        onClick={() => revealFunc("")}></i>
                </button>
            </div>
        </div>
    );
};

Delete.propTypes = {
    extraClasses: PropTypes.string,
    revealFunc: PropTypes.func,
    onClick: PropTypes.func,
    type: PropTypes.string,
};

export default Delete;
