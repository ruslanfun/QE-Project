import React from 'react';

const Step3 = ({ form, onSubmit, isPosting }) => {
  return (
    <div>
      <h1>Step 3</h1>

      <dl>
        <dt>Email</dt>
        <dd>{form.email}</dd>
        <dt>First name</dt>
        <dd>{form.firstName}</dd>
        <dt>Last name</dt>
        <dd>{form.lastName}</dd>
      </dl>

      <form onSubmit={onSubmit}>
        {isPosting ?
          <button type='button' className='btn btn-primary' disabled>
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </button> :
          <button type='submit' className='btn btn-primary'>Submit</button>
        }
      </form>

    </div>
  );
}

export default Step3;
